from config.config import *
import os
from time import sleep
import platform
def cl():
    if platform.system() == "Linux":
        return "clear"
    elif platform.system() == "Windows":
        return "cls"

while True:
    os.system(cl())
    inp = input("print city code: ").strip()
    out = cityCode[inp]
    print(out)
    sleep(10)
