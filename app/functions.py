import platform as plt
import os
import pendulum
from humanfriendly.tables import format_pretty_table as format_table
from hashlib import md5


def clear():
    return os.system("cls") if plt.system() == "Windows" else os.system("clear")


def print_table(text, column, data, /, border="■", *, width=50):
    clear()
    print(f" {text} ".center(width, border))
    print(format_table(data, column))


def headline(text, /, border="■", *, width=50):
    # clear()
    print(f" {text} ".center(width, border))


def encode_md5(password):
    return md5(password.encode("utf-8")).hexdigest()


def get_date_today():
    return pendulum.now("Asia/Jakarta")
