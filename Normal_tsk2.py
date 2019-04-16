#NORMAL
# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system
#
BASE_PATH = r".\HWGB_5\Normaltsk5.py"
import os

M = int(input("Input M number repeat cycle:  "))
for i in range(M):
    N = int(input("Input N:  "))
    S = input("Input S:  ")
    os.system(f"python.exe {os.path.abspath(BASE_PATH)} {N} {S}")
