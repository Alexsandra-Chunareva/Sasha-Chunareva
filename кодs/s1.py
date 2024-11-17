from time import process_time

def time_decorator(func):
    def wrapper():
        start_time = process_time()
        result = func()
        end_time = process_time()
        print(f"\nВремя выполнения функции: {end_time - start_time} секунд")
        return result
    return wrapper

@time_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

if __name__ == "__main__":
    fibonacci()
