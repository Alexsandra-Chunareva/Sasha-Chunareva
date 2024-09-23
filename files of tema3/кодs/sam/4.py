def manipulate_string(sentence):
    print("Длина предложения:", len(sentence))
    lowercase_sentence = sentence.lower()
    print("Предложение в нижнем регистре:", lowercase_sentence)
    vowels = 'aeiou'
    count_vowels = sum(char in vowels for char in sentence)
    print("Количество гласных:", count_vowels)
    modified_sentence = sentence.replace('ugly', 'beauty')
    print("Замененное предложение:", modified_sentence)
    if sentence.startswith('the'):
        print("Предложение начинается с 'The'.")
    else:
        print("Предложение не начинается с 'The'.")
    if sentence.endswith('end'):
        print("Предложение заканчивается на 'end'.")
    else:
        print("Предложение не заканчивается на 'end'.")
while True:
    sentence = input("Введите предложение: ")
    manipulate_string(sentence)
    answer = input("Хотите ввести еще одно предложение? (да/нет): ")
    if answer == 'нет':
        break