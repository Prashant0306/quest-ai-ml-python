# ============================================
# utils/__init__.py  ->  makes 'utils' a PACKAGE
# ============================================
# A "package" is a folder of modules containing an __init__.py file.
# This file runs when the package is first imported.
#
# By re-exporting names here, callers can write the short form:
#     from utils import add, format_box
# instead of the longer:
#     from utils.numbers import add
#     from utils.strings import format_box

from .numbers import add, multiply
from .strings import format_box, shout
from .stocks import get_todays_price

# __all__ controls what 'from utils import *' brings in.
__all__ = ["add", "multiply", "format_box", "shout", "get_todays_price"]
