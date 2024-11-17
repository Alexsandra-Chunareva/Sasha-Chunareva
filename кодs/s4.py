class CallLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Вызов функции: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"Результат: {result}\n")
        return result
@CallLogger
def reverse_string(s):
    return s[::-1]

@CallLogger
def multiply_by_ten(n):
    return n * 10

print("Тест 1: Переворот строки 'hello'")
reverse_string("hello")

print("Тест 2: Умножение числа 5 на 10")
multiply_by_ten(5)
