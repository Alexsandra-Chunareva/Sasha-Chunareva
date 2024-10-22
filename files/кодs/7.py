lines = ['one', 'two', 'three']
with open('i.txt', 'w') as f:
    for line in lines:
        f.write('\nsurpraizik ' + line)
    print('Done!')