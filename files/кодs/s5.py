def set_gen(lst):
    index = 0
    while index < len(lst):
        cnt = lst.count(lst[index])
        if cnt > 1:
            lst[index] = str(lst[index]) * cnt
        index += 1
    return set(lst)
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))