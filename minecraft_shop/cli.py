from dotenv import load_dotenv
from os import environ, listdir, path
import inquirer

from __init__ import SHOP_FOLDER, VILLAGER_FOLDER
from util import load_yaml


def env_init():
    global SHOP_FOLDER
    global VILLAGER_FOLDER

    load_dotenv()

    SHOP_FOLDER = environ.get("SHOP_FOLDER")
    VILLAGER_FOLDER = environ.get("VILLAGER_FOLDER")

    if SHOP_FOLDER is None or VILLAGER_FOLDER is None:
        print("ERROR SHOP_FOLDER and VILLAGER_FOLDER env vars must be defined")
        exit(1)


def prompt_input():
    available_shops = [
        path.splitext(p)[0] for p in listdir(path.join(SHOP_FOLDER, "shops"))
    ]
    available_villagers = [
        (
            load_yaml(path.join(VILLAGER_FOLDER, "Shops", p)).entity.name[2:],
            path.splitext(p)[0],
        )
        for p in listdir(path.join(VILLAGER_FOLDER, "Shops"))
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
