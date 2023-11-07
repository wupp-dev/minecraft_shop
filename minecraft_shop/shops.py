from util import load_yaml
from os import path

from __init__ import SHOP_FOLDER


def get_category(category: str):
    p = path.join(SHOP_FOLDER(), "shops", category + ".yml")
    yaml = load_yaml(p)

    items = []
    for page in yaml["pages"]:
        items += list(yaml["pages"][page]["items"].values())

    return items
