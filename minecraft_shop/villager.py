from os import path
from util import load_yaml


class Villager:
    items = []
    base_config = None

    def __init__(self, this_id: str, load_base=False):
        self.villager_id = this_id

    def config_path(self) -> str:
        return path.join(
            "/home/hipy/dev/server/minecraft_shop/VillagerMarket/Shops",
            self.villager_id + ".yml",
        )

    def load_base_config(self):
        self.base_config = load_yaml(self.config_path())

    def push_items(self, items: list):
        self.items += items

    def replace_items(self, items: list):
        self.items = items

    def get_items(self):
        return self.items
