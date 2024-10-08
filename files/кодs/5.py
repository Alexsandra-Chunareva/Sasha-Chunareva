def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 5, 7, 3, 33]))
print(useless([-77, 7, -35, 4.9]))
print(useless([-1, 0.999, -600, 15]))