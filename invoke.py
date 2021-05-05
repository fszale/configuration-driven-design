import yaml
from src.build import BuildProduct
import src.common.config
from dotty_dict import dotty
import sys


if __name__ == "__main__":

    configFile = sys.argv[1:][0]
    if configFile is None:
        print('Missing configuration parameter')
        exit(1)

    bp = BuildProduct()

    src.common.config.data = dotty(yaml.load(open(configFile), yaml.FullLoader))

    bp.start(src.common.config.data)

