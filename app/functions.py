import platform
import os
import time


def clear():
    return os.system("cls") if platform.system() == "Windows" else os.system("clear")


def headline(text, /, border="♦", *, width=50):
    time.sleep(0.5)
    clear()
    print(f" {text} ".center(width, border))