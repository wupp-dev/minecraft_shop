from dotenv import load_dotenv
from os import environ, listdir, path
import inquirer

from __init__ import VILLAGER_FOLDER, SHOP_FOLDER
from util import load_yaml
from shops import get_category
from villager import Villager


def env_init():
    load_dotenv()

    shop_folder = environ.get("SHOP_FOLDER")
    villager_folder = environ.get("VILLAGER_FOLDER")

    if shop_folder is None or villager_folder is None:
        print("ERROR SHOP_FOLDER and VILLAGER_FOLDER env vars must be defined")
        exit(1)


def prompt_input():
    available_shops = [
        path.splitext(p)[0] for p in listdir(path.join(SHOP_FOLDER(), "shops"))
    ]
    available_villagers = [
        (
            load_yaml(path.join(VILLAGER_FOLDER(), "Shops", p)).entity.name[2:],
            path.splitext(p)[0],
        )
        for p in listdir(path.join(VILLAGER_FOLDER(), "Shops"))
    ]

    selected = inquirer.prompt(
        [
            inquirer.List(
                "shop",
                message="Select shop category to load items and prices",
                choices=available_shops,
            ),
            inquirer.List(
                "villager",
                message="Select a villager to apply the shop",
                choices=available_villagers,
            ),
        ]
    )

    return selected


def main():
    selected = prompt_input()

    shop_items = get_category(selected["shop"])

    villager = Villager(selected["villager"])

    villager.replace_items(shop_items)

    villager.save_to_file()

    print(
        f"Saved in villager {villager.villager_id} ({villager.config_path()}) {len(villager.items)} items"
    )
