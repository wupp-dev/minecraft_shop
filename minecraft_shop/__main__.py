import inquirer
from dotenv import load_dotenv, dotenv_values

from shops import get_category
from villager import Villager
from cli import env_init, prompt_input

env_init()

selected = prompt_input()
print(selected)

shop_items = get_category(selected["shop"])

villager = Villager(selected["villager"])

villager.replace_items(shop_items)
