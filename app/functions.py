from humanfriendly.tables import format_pretty_table as format_table
from hashlib import md5

import platform as plt
import os
import pendulum
import pytz


def clear():
    return os.system("cls") if plt.system() == "Windows" else os.system("clear")


def print_table(text, column, data, /, border="■", *, width=50):
    clear()
    print(f" {text} ".center(width, border))
    print(format_table(data, column))


def headline(text, /, border="■", *, width=50):
    print(f" {text} ".center(width, border))


def encode_md5(password):
    return md5(password.encode("utf-8")).hexdigest()


def get_date_today():
    return pendulum.now("Asia/Jakarta")


def count_days(datetime_start, datetime_end):
    utc = pytz.UTC
    datetime_start = utc.localize(datetime_start)
    datetime_end = utc.localize(datetime_end)

    delta = datetime_end - datetime_start
    return delta.days
