import os

nameDataFolder = "Data_PyQt5"

a = input("num")
os.system(f"python -m PyQt5.uic.pyuic -x ./PyQt5/{a}.ui -o ./{nameDataFolder}/output.py")
