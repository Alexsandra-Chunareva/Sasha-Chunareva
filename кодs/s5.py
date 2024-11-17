class InvalidOperationError(Exception):
    #исключение, возникающее при попытке выполнить недопустимую операцию."""
    def __init__(self, message="Операция не может быть выполнена."):
        super().__init__(message)
#проверка деления на ноль
def divide(a, b):
    if b == 0:
        raise InvalidOperationError("Деление на ноль невозможно.")
    return a / b
#проверка диапазона значений
def check_range(value, min_value=0, max_value=100):
    if value < min_value or value > max_value:
        raise InvalidOperationError(f"Значение {value} должно находиться в диапазоне от {min_value} до {max_value}.")
    return value

#тестирование нашего исключения
if __name__ == "__main__":
    #тестирование для деления
    try:
        result = divide(10, 0)
    except InvalidOperationError as e:
        print(e)
    #нормальное деление
    result = divide(50, 5)
    print(result)
    #тестирование проверки диапазона
    try:
        checked_value = check_range(-1)
    except InvalidOperationError as e:
        print(e)
    checked_value = check_range(75)
    print(checked_value)