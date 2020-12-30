import platform
import os
import time
from humanfriendly.tables import format_pretty_table as format_table
from hashlib import md5


def clear():
    return os.system("cls") if platform.system() == "Windows" else os.system("clear")


def print_table(text, column, data, is_clear=True, /, border="■", *, width=50):
    # if is_clear:
    # clear()
    print(f" {text} ".center(width, border))
    print(format_table(data, column))


def headline(text, /, border="■", *, width=50):
    # clear()
    print(f" {text} ".center(width, border))


def encode_md5(password):
    return md5(password.encode("utf-8")).hexdigest()