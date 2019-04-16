# NORMAL
# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system
#
# import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integer for number cyrcle print Text.')

parser.add_argument('Imput_Number', type=int, help='Integer for the cyrcle text')
parser.add_argument('Imput_String', type=str, help='String for String for repetitions on "N" numbers  ')

for i in range(parser.parse_args().Imput_Number):
    print(parser.parse_args().Imput_String)
