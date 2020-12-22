import platform
import os
import time
from humanfriendly import format_pretty_table


def clear():
    return os.system("cls") if platform.system() == "Windows" else os.system("clear")


def headline(text, /, border="♦", *, width=50):
    time.sleep(0.5)
    clear()
    print(f" {text} ".center(width, border))


def print_table(table, value):
    print(format_pretty_table(result, table))