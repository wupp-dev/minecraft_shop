from os import path
import yaml

from __init__ import VILLAGER_FOLDER
from util import load_yaml


class Villager:
    items = []
    base_config = None

    def __init__(
        self,
        this_id: str,
        load_base=False,
    ):
        self.villager_id = this_id

    def config_path(self) -> str:
        return path.join(
            VILLAGER_FOLDER(),
            "Shops",
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

    def save_to_file(self):
        self.load_base_config()
        out_yaml = self.base_config
        if not "items_for_sale" in out_yaml:
            out_yaml["items_for_sale"] = {}

        for i in range(0, len(self.items)):
            out_yaml["items_for_sale"][i] = {
                "item": {
                    "==": "org.bukkit.inventory.ItemStack",
                    "v": 3465,
                    "type": self.items[i]["material"],
                },
                "amount": 1,
                "trade_amount": 0,
                "price": self.items[i]["buy"],
                "buy_price": self.items[i]["sell"],
                "mode": "BUY_AND_SELL",
                "buy_limit": 0,
                "command": [],
                "server_trades": 0,
                "limit_mode": "PLAYER",
                "cooldown": "never",
                "discount": {"amount": 0, "end": 0},
                "next_reset": 0,
            }

        with open(self.config_path(), "w+") as wf:
            wf.write(out_yaml.to_yaml())
