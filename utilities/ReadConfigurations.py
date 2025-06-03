# from configparser import ConfigParser
#
# def read_configurations(category,key):
#     config = ConfigParser()
#     config.read('configurations/config.ini')
#     return config.get(category,key)

import os
from configparser import ConfigParser


def read_configurations(category, key):
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini')
    config.read(os.path.abspath(config_path))

    if not config.has_section(category):
        raise Exception(f"Missing section: {category}")
    if not config.has_option(category, key):
        raise Exception(f"Missing key: {key} in section: {category}")

    return config.get(category, key)
