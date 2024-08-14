
from const.parser_const import *

def watch_parse_channel(text, func):
    if len(text) == REGISTER_WIDTH_HEX:
        return func(text)
    return None
