# Тема 7. Работа с файлами (ввод, вывод)
Отчёт по теме выполнила:
  - Чунарёва Александра Дмитриевна
  - ПИЭ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + | 
| Задание 3 | + | + | 
| Задание 4 | + | + |
| Задание 5 | + | + | 
| Задание 6 | + | - | 
| Задание 7 | + | - | 
| Задание 8 | + | - | 
| Задание 9 | + | - | 
| Задание 10 | + | - | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторные задания:

### №1. 
Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
### Ответ (текст внутри файла):
```python
I am thankful for all of those who said NO to me.
It is because of them I am doing it myself.
                    (Albert Einstein)
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/1.png)

### №2. 
Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
### Ответ: 
```python
f = open('i.txt', 'r')
print(f.readline())
f.close()
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/2.png)

### Вывод: 
Этот код открывает файл i.txt для чтения ('r'), читает первую строку этого файла с помощью метода readline(), затем закрывает файл с помощью метода close().

### №3. 
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open(/)/close().
### Ответ: 
```python
f = open('i.txt', 'r')
print(f.readlines())
f.close()
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/3.png)

### Вывод: 
Этот код открывает файл i.txt для чтения ('r'), читает все строки этого файла с помощью метода readline(), затем закрывает файл с помощью метода close().

### №4. 
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
### Ответ: 
```python
with open ('i.txt') as f:
    print(f.readlines())
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/4.png)

### Вывод: 
Этот код открывает файл i.txt для чтения и затем выводит все строки этого файла. В результате выполнения этого кода будет выведен список строк, содержащихся в файле i.txt.

### №5. 
Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
### Ответ: 
```python
with open ('i.txt') as f:
    for line in f:
        print(line)
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/5.png)

### Вывод: 
Этот код открывает файл i.txt для чтения и обрабатывает каждую строку этого файла. Для каждой строки вызывается функция print(), которая выводит эту строку на экран.

### №6. 
Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
### Ответ: 
```python
with open('i.txt', 'a+') as f:
    f.write('\nO ma God, sameeeee')

with open('i.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/6.1.png)
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/6.2.png)

### Вывод: 
Этот код выполняет две операции с файлом i.txt. Во-первых, он открывает файл для записи, добавляет строку "\nO ma God, sameeeee" в конец файла и закрывает файл. Затем он снова открывает файл для чтения, читает все содержимое файла и выводит его на экран.

### №7. 
Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например, направит любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
### Ответ: 
```python
lines = ['one', 'two', 'three']
with open('i.txt', 'w') as f:
    for line in lines:
        f.write('\nsurpraizik ' + line)
    print('Done!')
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/7.1.png)
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/7.2.png)

### Вывод: 
Этот код записывает строки ['one', 'two', 'three'] в файл i.txt. Каждая строка предваряется текстом surpraizik, после чего следует новая строка. После завершения записи выводится сообщение Done!.

### №8. 
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
### Ответ: 
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:/Users/alchu/фотос')
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/8.png)

### Вывод: 
Функция print_docs принимает путь к директории и использует метод os.walk, чтобы получить информацию обо всех файлах и поддиректориях в данной директории. Она печатает название папки, список директорий внутри нее и список файлов. В конце выводится горизонтальная линия для визуального разделения информации.

### №9. 
Документ «input.txt» содержит следующий текст:
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.

Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). 
### Ответ: 
```python
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
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/9.1.png)

### Вывод: 
Функция longestwords принимает файл в качестве аргумента и возвращает самое длинное слово в этом файле. Она открывает файл, читает его содержимое, разбивает строку на слова и определяет максимальную длину слова. Затем она проходит по всем словам и выбирает те, которые имеют такую же длину, как и самое длинное слово. Если таких слов несколько, функция возвращает их все через пробел.

### №10. 
Требуется создать сsv-файл «rows_300.csv» со следующими столбцами:
. № – номер по порядку (от 1 до 300);
. Секунда – текущая секунда на вашем ПК;
. Микросекунда – текущая миллисекунда на часах.
Для наглядности на каждой интерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
### Ответ: 
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        dt = datetime.datetime.now()
        writer.writerow([line, dt.second, dt.microsecond])

time.sleep(0.01)
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/10.1.png)
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/10.2.png)
#### Файл «rows_300.csv» также есть в папке "кодs"

### Вывод: 
Этот код Python создает файл rows_300.csv с 300 строками данных, каждая из которых содержит номер строки, секунды и микросекунды текущего времени. Используются модули csv, datetime и time. Сначала создается объект CSV-писателя для записи данных в файл. Затем выполняется цикл, который записывает данные для каждой строки, включая текущие значения секунд и микросекунд. После завершения цикла происходит пауза в 0.01 секунды перед завершением программы.

## Самостоятельные задания:

### №1. 
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
### Ответ: 
```python
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
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s1.1.png)
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s1.2.png)

### Вывод: 
Функция number_of_words принимает файл file в качестве аргумента и выполняет следующие шаги:

1. Открывает файл для чтения в кодировке UTF-8.
2. Проходит по каждой строке и преобразует её в нижний регистр, после чего разбивает на отдельные слова.
3. Для каждого слова проверяет, есть ли оно уже в словаре word_count, и обновляет счётчик этого слова.
4. Сохраняет длину каждой строки в список summa.
5. Выводит количество всех слов в статье.
6. Определяет самое часто встречающееся слово и количество его повторений.
7. Печатает информацию о самом частом слове и количестве его повторений.
   
### №2. 
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
### Ответ: 
```python
def add():
    description = input("Назначение расходов: ")
    amount = input("Сумма расходов: ")
    with open('s2.txt', 'a', encoding='utf-8') as file:
        file.write(f'{description}: {amount}\n')
def show():
    print("Записи расходов:")
    with open('s2.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
while True:
    action = input("Введите 'добавить' для добавления расхода или 'показать' для вывода всех расходов: ").strip()
    if action.lower() == 'добавить':
        add()
    elif action.lower() == 'показать':
        show()
    else:
        print("Неверный ввод. Попробуйте снова.")
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s2.1.png)
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s2.2.png)

### Вывод: 
Этот код на Python позволяет пользователю добавлять и просматривать записи о расходах. Функция add() принимает назначение расходов и сумму через стандартный ввод и записывает их в файл s2.txt. Функция show() считывает содержимое этого файла и выводит его на экран. Основной цикл предоставляет выбор между действиями 'добавить' и 'показать'.

### №3. 
Имеются файл s3.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
- Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
- Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines
### Ответ: 
```python
def text_statistics(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    letters_count = sum(c.isalpha() for c in text)
    words_count = len(text.split())
    lines_count = text.count('\n') + 1
    print(f"Input file contains:")
    print(f"{letters_count} letters")
    print(f"{words_count} words")
    print(f"{lines_count} lines")
text_statistics('s3.txt')
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s3.1.png)

### Вывод: 
Функция text_statistics принимает на вход имя файла и возвращает количество букв, слов и строк в этом файле. Она использует метод file.read() для чтения содержимого файла, а затем применяет несколько операций для подсчета соответствующих значений. После этого результаты выводятся на экран.

### №4. 
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звёздочками (* количество звёздочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встретились, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит следующее слово exam, то слова экзамен, Exam, ExaM, EXAM и exAm должны быть замены на ****.
- Запрещенные слова:
hello email python the exam wor is
- Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My EMAIL is... PYTHON is awesome!!!
- Ожидаемый результат:
 hello    the   is
*****, ***ld! ****** ** *** programming language of *** future. My ***** **... ****** ** awesome!!!

### Ответ: 
```python
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
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s4.2.png)

### Вывод: 
Функция censor_text принимает два аргумента: строку input_text и список запрещенных слов banned_words. Она использует регулярное выражение для поиска каждого слова из списка banned_words в строке input_text, заменяет каждое найденное слово символами '*' в количестве, равном длине этого слова, и возвращает измененную строку. Входная строка читается из файла input.txt, который содержит список запрещенных слов. Затем пользователь вводит предложение, которое обрабатывается функцией censor_text, и результат отображается на экране.

### №5. 
Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
#### Задача: Создать программу для наглядного представления данных по приемам пищи. 

### Ответ: 
```python
def add():
    meal = input("Прием пищи: ")
    description = input("Краткое описание блюд: ")
    kalo = input("Калорийность: ")
    with open('s5.txt', 'a', encoding='utf-8') as file:
        file.write(f'{meal} ({description}) : {kalo}\n')
def show():
    print("Приемы пищи:")
    with open('s5.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
while True:
    action = input("Введите '1' для добавления данных о приеме пищи или '0' для вывода всех данных: ").strip()
    if action.lower() == '1':
        add()
    elif action.lower() == '0':
        show()
    else:
        print("Неверный ввод. Попробуйте снова.")
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema7/files/screen/s5.png)

### Вывод: 
Программа создана для более наглядного и удобного контроля потреблённых блюд и их калорийности. Программа позволяет ввести название приема пищи, его содержание и калорийность. А после вывести полную сводку приемов пищи.
## Общий вывод по теме: 

В заключение можно сказать, что работа с файлами — это неотъемлемая часть любой программы. 
Для эффективного управления файлами необходимо знать основные операции, режимы доступа и методы работы с содержимым.

Основные операции с файлами:

- Открытие файла с помощью функции open().
- Чтение данных из файла с использованием методов read(), readline(), readlines().
- Запись данных в файл с помощью метода write().
- Добавление данных в файл в режиме «a».
- Закрытие файла с помощью метода close().

Режимы доступа к файлу:

«r» — только чтение.
«w» — только запись.
«a» — добавление данных в конец файла.
«b» — бинарный режим.
«t» — текстовый режим.
«+» — режим чтения/записи.

Рекомендуемые практики:

Использование конструкции with open() для автоматического закрытия файла.
Обработка исключений при работе с файлами с помощью try-except-finally.
Правильное закрытие файлов после использования.

Методы работы с содержимым:

- readline() — чтение одной строки.
- readlines() — чтение всех строк в список.
- write() — запись данных.
- seek(), tell() — управление указателем чтения/записи.
- flush() — принудительная запись буфера.

Правильная работа с файлами позволяет избежать утечки ресурсов и обеспечить корректную обработку данных в программе.
