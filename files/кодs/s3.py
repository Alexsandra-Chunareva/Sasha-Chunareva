import math

def heron_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area)

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [2, 21, 37, 56, 84]

def find_max_min(lst):
    return max(lst), min(lst)

max_one, min_one = find_max_min(one)
max_two, min_two = find_max_min(two)
max_three, min_three = find_max_min(three)

area1 = heron_area(max_one, max_two, max_three)
area2 = heron_area(min_one, min_two, min_three)

print("Площадь первого треугольника:", area1)
print("Площадь второго треугольника:", area2)