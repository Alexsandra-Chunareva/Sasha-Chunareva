from collections import Counter
def count_repeating_numbers(sequence):

    numbers_counts = Counter(sequence)
    most_common_numbers = numbers_counts.most_common(3)
    for key, value in sorted(most_common_numbers, key = lambda x: x[0]):
        print('Число:', key , 'Встречается столько раз:', value)

sequence = '955687904333784999'
count_repeating_numbers(sequence)