import re
def censor_text(input_text, banned_words):
    for word in banned_words:
        input_text = re.sub(word, '*' * len(word), input_text, flags=re.IGNORECASE)
    return input_text
with open('s4.txt', 'r', encoding='utf-8') as file:
    banned_words = file.read().strip().split()
sentence = input("Введите предложение для проверки: ")
censored_sentence = censor_text(sentence, banned_words)
print('Обработанное предложение', censored_sentence)