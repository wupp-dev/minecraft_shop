from os import environ

SHOP_FOLDER = lambda: environ.get("SHOP_FOLDER")
VILLAGER_FOLDER = lambda: environ.get("VILLAGER_FOLDER")
