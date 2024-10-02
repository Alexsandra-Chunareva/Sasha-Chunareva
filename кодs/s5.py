from s5_triangle import heron

a = float(input("Введите первую сторону треугольника: "))
b = float(input("Введите вторую сторону треугольника: "))
c = float(input("Введите третью сторону треугольника: "))

area = heron(a, b, c)
if __name__ == '__main__':
    print(f"Площадь треугольника равна {area}")