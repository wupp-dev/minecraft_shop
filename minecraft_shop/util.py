import yaml
from box import Box


def load_yaml(path: str) -> Box:
    f = open(path, "r")
    y = yaml.safe_load(f)
    f.close()
    return Box(y)
