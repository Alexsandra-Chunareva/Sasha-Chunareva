def add_two_to_input():
    try:
        user_input = input("Введите число: ")
        number = int(user_input)
        result = 2 + number
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

print("Тест 1: Ввод корректного числа")
add_two_to_input()
print("\nТест 2: Ввод некорректного типа данных")
add_two_to_input()
print("\nТест 3: Ввод отрицательного числа ")
add_two_to_input()