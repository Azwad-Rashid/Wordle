'''Returns a custom font'''

from load_config import config_data

def custom_font(size: int, bold: bool = False) -> tuple[str, int, str]:
    '''Returns a tuple to select font
    
    :param size: The font size
    :type size: int
    :param bold: Whether the font will be bold or not
    :type bold: bool
    '''

    return (config_data["WIDGETS"]["font_family"], size, "bold" if bold else "normal")