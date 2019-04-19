
import os
import shutil

BASE_PATH = r"C:\Users\vitaliy.prokudin\Downloads\Telegram Desktop"
POINT_PATH = r"C:\Users\vitaliy.prokudin\Downloads"

# list_file = set()
# for file in os.listdir(BASE_PATH):
#     if os.path.isfile(os.path.join(BASE_PATH, file)):
#         list_file.add(os.path.splitext(file)[1])
#
# for e in list_file:
#     if not os.path.exists(os.path.join(BASE_PATH, e)):
#         os.mkdir(os.path.join(BASE_PATH, e))
#
# for file in os.listdir(BASE_PATH):
#     if os.path.isfile(os.path.join(BASE_PATH, file)):
#         os.rename(os.path.join(BASE_PATH, file), os.path.join(BASE_PATH, os.path.splitext(file)[1], file))

# Программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

list_dir = set(dir for dir in os.listdir(BASE_PATH))
for dir_format in list_dir:
    for file in os.listdir(os.path.join(BASE_PATH, dir_format)):
        os.rename(os.path.join(os.path.join(BASE_PATH, dir_format, file)), os.path.join(POINT_PATH, file))



