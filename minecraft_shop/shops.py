from util import load_yaml
from os import path


def get_category(category: str):
    p = path.join(
        "/home/hipy/dev/server/minecraft_shop/EconomyShopGUI/shops", category + ".yml"
    )
    yaml = load_yaml(p)

    items = []
    for page in yaml.pages:
        items += list(yaml.pages[page]["items"].values())

    return items
