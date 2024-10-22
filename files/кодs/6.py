with open('i.txt', 'a+') as f:
    f.write('\nO ma God, sameeeee')

with open('i.txt', 'r') as f:
    result = f.readlines()
    print(result)