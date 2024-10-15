def cortesh(incoming_list, number):
    if number not in incoming_list:
        return (0)
    if incoming_list.count(number) == 1:
        return incoming_list[incoming_list.index(number):]
    return incoming_list[incoming_list.index(number):incoming_list.index(number, incoming_list.index(number) + 1) + 1]


print(cortesh((1, 2, 3), 8))
print(cortesh((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(cortesh((1, 2, 8, 5, 1, 2, 9), 8))