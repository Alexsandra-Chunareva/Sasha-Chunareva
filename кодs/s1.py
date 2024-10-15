input_string = input('Введите числа через пробел: ')

numbers_list = list(map(int, input_string.split()))
numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)