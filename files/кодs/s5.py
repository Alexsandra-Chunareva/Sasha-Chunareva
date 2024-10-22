def add():
    meal = input("Прием пищи: ")
    description = input("Краткое описание блюд: ")
    kalo = input("Калорийность: ")
    with open('s5.txt', 'a', encoding='utf-8') as file:
        file.write(f'{meal} ({description}) : {kalo}\n')
def show():
    print("Приемы пищи:")
    with open('s5.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
while True:
    action = input("Введите '1' для добавления данных о приеме пищи или '0' для вывода всех данных: ").strip()
    if action.lower() == '1':
        add()
    elif action.lower() == '0':
        show()
    else:
        print("Неверный ввод. Попробуйте снова.")