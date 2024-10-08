def fix_grades(grades):
    grades = [grade for grade in grades if grade != 2]
    return [4 if grade == 3 else grade for grade in grades]

list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

result1 = fix_grades(list1)
result2 = fix_grades(list2)
result3 = fix_grades(list3)

print(f"После обработки списка 1: ", result1)
print(f"После обработки списка 2: ", result2)
print(f"После обработки списка 3: ", result3)