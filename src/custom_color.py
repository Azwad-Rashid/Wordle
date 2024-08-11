'''Returns a custom color'''

from load_config import config_data

def custom_color(name: str) -> str:
    '''Returns the hex code of the requested color
    
    :param name: Name of the required color
    :type name: str
    '''

    colors: list[str] = config_data["COLORS"]

    match name:
        case "background":
            return colors[name]
        case "bg":
            return colors["background"]
        case "white":
            return colors[name]
        case "black":
            return colors[name]
        case "grey":
            return colors[name]
        case "yellow":
            return colors[name]
        case "green":
            return colors[name]
        case "red":
            return colors[name]
        case _:
            return "#ffffff" # Just returns white if the requested color is not found