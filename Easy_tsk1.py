# HWGB_5
# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует
# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.
import os
import psutil

# Define
def Current_dir():
    # global Menu, command
    print(os.listdir())
    # print_menu(Menu)
    # command = get_command(Menu)


def Exit():
    print(f"Good Bay {os.getlogin()}")


def Add_dir():
    current_dir= os.getcwd()
    print(current_dir)
    print(os.listdir())
    input_enter=input("Enter dir for transition or <Enter> if create Dir hear:  ")
    os.chdir(f"{current_dir}\{input_enter}")
    print(current_dir)
    print(os.listdir())
    input_enter_1=input("Create dir1-9 YES/NO:  ")
    if input_enter_1=="yes":
        for i in range(9):
            os.mkdir(f"dir_{i}")
        print("Create successful dir1-9")
    else:
        print("Error Create dir ")


def Delete_dir():
    print(os.listdir())
    input_enter_1 = input("Delete dir1-9 YES/NO:  ")
    if input_enter_1=="yes":
        try:
            for i in range(9):
                os.rmdir(f"dir_{i}")
                print("Delete successful dir1-9")
        except Exception:
            print("Dir not found or Dir not empty")
    else:
        print("Error delete dir")


def print_menu(Menu):
    for i, n in enumerate(Menu, start=1):
        print(f"{i}.{n}")


def get_command(Menu):
    answer = int(input("Enter menu: "))
    if answer <= len(Menu):
        return answer - 1
    else:
        return -1

#Main

Menu = ["Current dir", "Add dir", "Delete dir", "Exit"]
Commands = [Current_dir, Add_dir, Delete_dir, Exit]
command=None

while command!=3:
    print_menu(Menu)
    command = get_command(Menu)

    if command == -1:
        print("Wrong command")

    Commands[command]()






