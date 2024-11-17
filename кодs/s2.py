import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        os.system('echo Файл не найден')

if __name__ == "__main__":
    file_name = 'f2.txt'
    data = read_file(file_name)
    if data:
        print("Информация из файла:\n", data)
    else:
        print("Файл пустой")

if __name__ == "__main__":
    file_name = 'ff2.txt'
    data = read_file(file_name)
    if data:
        print("Информация из файла:\n", data)
    else:
        print("Файл пустой")
