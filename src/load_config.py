import configparser

config = configparser.ConfigParser()
config.read("src/config.ini")

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
    - width
    - height
    - topmost
    - background
- WIDGETS
    - font_family
    - font_size
    - black
    - grey
    - yellow
    - green
'''
