for i in range(10):
    print('i = ', i)
    if i == 0:
        i += 2
    if i == 1:
        continue
    if i == 2 or i == 3:
        print('Переменная равна 2 или 3.')
    elif i in [4, 5, 6]:
        print('Переменная равна 4, 5 или 6.')
    else:
        break