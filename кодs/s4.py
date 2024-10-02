def calculate_average(args):
    total = sum(args)
    return total / len(args)

if __name__ == '__main__':
    args = list(map(float, input('Введите значения: ').split()))
    average = calculate_average(args)
    print(f'Среднее арифметическое: {average}')