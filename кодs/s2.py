def remover(tup, elem):
    try:
        index = tup.index(elem)
        new_tuple = list(tup)
        del new_tuple[index]
        return tuple(new_tuple)
    except ValueError:
        return tup

print(remover((1, 2, 3), 1))
print(remover((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remover((2, 4, 6, 6, 4, 2), 9))
