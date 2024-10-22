def number_of_words(file):
    words = []
    summ = []
    word_count = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower().split()
            len_of_line = len(line)
            words.append((line, len_of_line))

            for word in line:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        for i, v in words:
            summ.append(v)
        print(f'Всего слов в статье: {sum(summ)}')
    word_with_maximus = max(word_count, key=word_count.get)
    maximus = max(word_count.values())
    print(f'Cамое часто повторяющееся слово в тексте: {word_with_maximus}\nОно повторяется: {maximus} раз')
number_of_words('ss.txt')