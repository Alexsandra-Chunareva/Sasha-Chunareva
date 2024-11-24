def fib(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib200 = list(fib(200))
print(fib200[-1])