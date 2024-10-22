def longestwords(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

            if len(sought_words) == 1:
                return ' '.join([sought_words])
            return sought_words


print(longestwords('input.txt'))