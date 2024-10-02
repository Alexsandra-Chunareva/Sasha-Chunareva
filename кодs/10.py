global result

def rectangle():
    a = float(input("Ширина = "))
    b = float(input("Высота = "))
    global result
    result = a*b

def triangle():
    a = float(input("Основание = "))
    h = float(input("Высота = "))
    global result
    result = 0.5*a*h

figure = input("1-й прямоугольник, 2-й треугольник: ")

if __name__ == '__main__':
    if figure == '1':
        rectangle()
    elif figure == '2':
        triangle()

print(f"Площадь: {result}")