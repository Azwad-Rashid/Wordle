'''Loads the data from a config.ini file'''

import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath("config.ini"))

config_data: dict[str, dict[str, str]] = {
    section: {
        data[0]: data[1] for data in config[section].items()
        } for section in config.sections()}
'''Dict containing config data

Contains
--------
- GENERAL
    - app_name
    - author
    - version
- WINDOW
    - topmost
    - background
- WIDGETS
    - font_family
    - font_size
- COLORS
    - black
    - grey
    - yellow
    - green
'''
