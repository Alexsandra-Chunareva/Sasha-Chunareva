# Тема 8. Введение в ООП
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

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторные задания:

### №1. 
Создайте класс "Car" с атрибутами производитель и модель. Создайте объект этого класса. Напишите компоненты для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с компонентами.
### Ответ: 
```python
class Car:  # Определение класса 'Car'
    def __init__(self, make, model):  # Метод инициализации экземпляра класса
        self.make = make  # Присваивание значения параметра 'make' атрибуту 'make' объекта
        self.model = model  # Присваивание значения параметра 'model' атрибуту 'model' объекта

# Создание экземпляра класса 'Car' с параметрами 'Toyota' и 'Corolla'
my_car = Car("Toyota", "Corolla")
# Вывод информации об автомобиле на экран
print(f"Бренд: {my_car.make}, Модель: {my_car.model}")
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/1.png)

### Вывод: 
В этом коде описывается класс Car, который представляет автомобиль. У класса есть конструктор __init__, который принимает два параметра: марку автомобиля (make) и модель (model). Эти параметры сохраняются в соответствующих атрибутах экземпляра класса. Затем создаётся объект my_car класса Car с параметрами "Toyota" и "Corolla". В конце выводится информация о бренде и модели этого автомобиля.

### №2. 
Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
### Ответ: 
```python
# Определение класса Car
class Car:
    # Метод инициализации, который вызывается при создании нового экземпляра класса
    def __init__(self, make, model):
        # Сохранение марки автомобиля в атрибуте 'make'
        self.make = make
        # Сохранение модели автомобиля в атрибуте 'model'
        self.model = model

    # Метод для имитации вождения автомобиля
    def drive(self):
        # Вывод сообщения о вождении текущего автомобиля
        print(f"Driving the {self.make} {self.model}")

# Создание экземпляра класса Car с маркой Toyota и моделью Corolla
my_car = Car("Toyota", "Corolla")
# Вызов метода drive у созданного экземпляра my_car
my_car.drive()
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/2.png)

### Вывод: 
В данном коде создается класс Car, который представляет автомобиль. У класса есть два атрибута: марка (make) и модель (model), которые задаются при инициализации экземпляра через метод __init__. Также у класса есть метод drive, который выводит сообщение о том, что автомобиль движется. В конце кода создается экземпляр класса Car для автомобиля марки Toyota модели Corolla, после чего вызывается метод drive.

### №3. 
Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
### Ответ: 
```python
# Определение класса Car, который представляет автомобиль
class Car:
    # Метод инициализации экземпляра класса Car
    def __init__(self, make, model):
        # Сохранение марки автомобиля в атрибуте 'make'
        self.make = make
        # Сохранение модели автомобиля в атрибуте 'model'
        self.model = model
    # Метод для управления автомобилем
    def drive(self):
        # Вывод сообщения о вождении автомобиля
        print(f"Driving the {self.make} {self.model}")

# Класс ElectricCar, наследующий от класса Car
class ElectricCar(Car):
    # Метод инициализации экземпляра класса ElectricCar
    def __init__(self, make, model, battery_capacity):
        # Вызов метода инициализации родительского класса Car
        super().__init__(make, model)
        # Сохранение емкости батареи в атрибуте 'battery_capacity'
        self.battery_capacity = battery_capacity
    # Метод зарядки электромобиля
    def charge(self):
        # Вывод сообщения о зарядке электромобиля
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

# Создание экземпляра класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 100)
# Вызов метода вождения для созданного экземпляра
my_electric_car.drive()
# Вызов метода зарядки для созданного экземпляра
my_electric_car.charge()
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/3.png)

### Вывод: 
В данном коде реализованы два класса: Car и ElectricCar. Класс Car представляет собой базовый класс для автомобиля, который имеет марку (make) и модель (model), а также метод drive, который выводит сообщение о вождении данного автомобиля. Класс ElectricCar является наследником от Car, добавляет параметр батареи (battery_capacity) и метод charge, который позволяет зарядить электромобиль. В конце кода создается экземпляр ElectricCar, вызываются методы drive и charge.

### №4. 
Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
### Ответ: 
```python
class Car:  # Определение класса 'Car'
    def __init__(self, make, model):  # Конструктор класса, вызывается при создании экземпляра
        self._make = make  # Присваивание значения аргумента 'make' переменной экземпляра '_make'
        self.__model = model  # Присваивание значения аргумента 'model' переменной экземпляра '__model' (с использованием двойного подчеркивания для создания "псевдо-приватной" переменной)
    def drive(self):  # Метод класса, который выводит сообщение о вождении автомобиля
        print(f"Driving the {self._make} {self.__model}")  # Форматированный вывод строки с маркой и моделью автомобиля

# Создание экземпляра класса 'Car' с параметрами 'Toyota' и 'Corolla'
my_car = Car("Toyota", "Corolla")
# Доступ к защищённой переменной '_make' через экземпляр 'my_car'
print(my_car._make)
# Вызов метода 'drive' у экземпляра 'my_car', который выведет строку с маркой и моделью автомобиля
my_car.drive()
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/4.png)

### Вывод: 
Класс Car представляет собой модель автомобиля, которая имеет два атрибута: марку (_make) и модель (__model), а также метод drive, который выводит сообщение о вождении автомобиля. В примере создается объект класса Car, представляющий автомобиль марки Toyota модели Corolla, затем выводится марка автомобиля через публичный атрибут _make, после чего вызывается метод drive.

### №5. 
Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
### Ответ: 
```python
# Определение базового класса для геометрических фигур
class Shape:
    # Абстрактный метод для вычисления площади фигуры
    def area(self):
        pass

# Класс прямоугольника, наследующий от класса Shape
class Rectangle(Shape):
    # Конструктор класса, принимающий ширину и высоту прямоугольника
    def __init__(self, width, height):
        # Сохранение ширины и высоты в экземпляре класса
        self.width = width
        self.height = height
    # Метод для вычисления площади прямоугольника
    def area(self):
        # Возвращает произведение ширины и высоты
        return self.width * self.height

# Класс круга, также наследующий от класса Shape
class Circle(Shape):
    # Конструктор класса, принимающий радиус круга
    def __init__(self, radius):
        # Сохранение радиуса в экземпляре класса
        self.radius = radius
    # Метод для вычисления площади круга
    def area(self):
        # Возвращает площадь круга по формуле π * r^2
        return 3.14 * self.radius ** 2

# Создание списка объектов фигур (прямоугольник и круг)
shapes = [Rectangle(4, 5), Circle(5)]
# Проход по всем фигурам в списке и вывод их площадей
for shape in shapes:
    # Вывод строки с площадью текущей фигуры
    print(f"Площадь: {shape.area()}")
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/5.png)

### Вывод: 
В этом коде демонстрируется использование полиморфизма через наследование классов. Класс Shape является базовым классом для фигур, а классы Rectangle и Circle наследуют от него и переопределяют метод area(), чтобы вычислять площадь фигуры. В основной части программы создается список объектов разных типов (Rectangle и Circle), после чего с помощью цикла выполняется вызов метода area() для каждого объекта, что позволяет вычислить их площади без необходимости знать конкретный тип фигуры.

## Самостоятельные задания:

### №1. 
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
### Ответ: 
```python
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Количество страниц: {self.pages}")

my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 1966, 480)

my_book.display_info()

```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/s1.png)

### Вывод: 
Этот код определяет класс Book с атрибутами для хранения информации о книге и методом display_info, который выводит эту информацию на экран. Затем создается объект my_book и вызывается метод для отображения данных о книге.

### №2. 
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
### Ответ: 
```python
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_read = False

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Жанр: {self.genre}")
        print(f"Прочитана: {'Да' if self.is_read else 'Нет'}")

    def mark_as_read(self):
        if self.is_read == True:
            print(f"Книга '{self.title}' отмечена как прочитанная.")
        else:
            print(f"Книга '{self.title}' отмечена как непрочитанная.")

    def display_short_info(self):
        print(f"'{self.title}' - {self.author} ({self.year}) [{self.genre}]")

my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 1966,  "Роман")
my_book.display_info()
my_book.mark_as_read()
my_book.display_short_info()

```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/s2.png)

### Вывод: 
Этот код создает класс Book, представляющий информацию о книге. Класс включает атрибуты для хранения данных о названии, авторе, годе издания, жанре и статусе прочтения. Также добавлены методы:
display_info() — выводит полную информацию о книге.
mark_as_read() — отмечает книгу как прочитанную.
display_short_info() — выводит краткую информацию о книге.
Объект my_book создается с определенными атрибутами, после чего вызываются методы для отображения полной информации о книге, изменения статуса прочтения и отображения краткой информации.
### №3. 
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
### Ответ: 
```python
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_read = False

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Жанр: {self.genre}")
        print(f"Прочитана: {'Да' if self.is_read else 'Нет'}")

    def mark_as_read(self):
        if self.is_read == True:
            print(f"Книга '{self.title}' отмечена как прочитанная.")
        else:
            print(f"Книга '{self.title}' отмечена как непрочитанная.")

    def display_short_info(self):
        print(f"'{self.title}' - {self.author} ({self.year}) [{self.genre}]")

class EBook(Book):
    def __init__(self, title, author, year, genre, file_size, file_format):
        super().__init__(title, author, year, genre)
        self.file_size = file_size
        self.file_format = file_format

    def display_ebook_info(self):
        self.display_info()
        print(f"Размер файла: {self.file_size} МБ")
        print(f"Формат файла: {self.file_format}")

my_ebook = EBook("Мастер и Маргарита", "Михаил Булгаков", 1966, "Роман", 2.5, "PDF")

my_ebook.display_ebook_info()
my_ebook.mark_as_read()

```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/s3.png)

### Вывод: 
Код создает класс Book, представляющий информацию о книге, и подкласс EBook, который расширяет Book дополнительными атрибутами для электронных книг (file_size и file_format). Класс EBook добавляет метод display_ebook_info для вывода всей информации, включая размер и формат файла. Создан объект my_ebook, который демонстрирует использование наследуемых и добавленных методов.

### №4. 
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
### Ответ: 
```python
class Book:
    def __init__(self, title, author, year, genre):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__genre = genre
        self.__is_read = False

    def display_info(self):
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        print(f"Год издания: {self.__year}")
        print(f"Жанр: {self.__genre}")
        print(f"Прочитана: {'Да' if self.__is_read else 'Нет'}")

    def is_book_read(self):
        return self.__is_read

    def mark_as_read(self):
        user_input = input(f"Прочитана ли книга '{self.__title}'? (Да/Нет): ")
        if user_input.lower() == 'да':
            self.__is_read = True
            print(f"Книга '{self.__title}' отмечена как прочитанная.")
        elif user_input.lower() == 'нет':
            self.__is_read = False
            print(f"Книга '{self.__title}' отмечена как непрочитанная.")
        else:
            print(f'Некорректный ввод')

    def display_short_info(self):
        print(f"'{self.__title}' - {self.__author} ({self.__year}) [{self.__genre}]")

class EBook(Book):
    def __init__(self, title, author, year, genre, file_size, file_format):
        super().__init__(title, author, year, genre)
        self.__file_size = file_size
        self.__file_format = file_format

    def display_ebook_info(self):
        self.display_info()
        print(f"Размер файла: {self.__file_size} МБ")
        print(f"Формат файла: {self.__file_format}")

    def get_file_size(self):
        return self.__file_size

    def set_file_size(self, size):
        if size > 0:
            self.__file_size = size
        else:
            print("Размер файла должен быть положительным числом.")

    def get_file_format(self):
        return self.__file_format

    def set_file_format(self):
        format_input = input("Введите формат файла (PDF, EPUB, MOBI): ")
        if format_input in ["PDF", "EPUB", "MOBI"]:
            self.__file_format = format_input
            print(f"Формат файла изменен на {self.__file_format}.")
        else:
            print("Неподдерживаемый формат файла.")

# Создание объекта класса EBook
my_ebook = EBook("Мастер и Маргарита", "Михаил Булгаков", 1966, "Роман", 2.5, "PDF")

# Вывод информации о книге
my_ebook.display_ebook_info()

# Ввод ответа на вопрос о прочтении книги
my_ebook.mark_as_read()

# Ввод нового формата файла
my_ebook.set_file_format()

```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/s4.png)

### Вывод: 
В этом коде реализованы классы `Book` и `EBook`, где `EBook` наследует функциональность `Book` и добавляет атрибуты, специфичные для электронной книги (размер и формат файла). В классе `Book` инкапсулированы атрибуты с использованием приватных переменных, доступ к которым осуществляется через методы-геттеры и сеттеры.

Программа запрашивает у пользователя:
1. Статус прочтения книги (`mark_as_read`), позволяя отметить книгу как прочитанную или непрочитанную.
2. Формат электронной книги (`set_file_format`), проверяя, является ли новый формат поддерживаемым.

Код демонстрирует инкапсуляцию и наследование, делая данные защищенными, и добавляет пользовательский ввод для изменения их состояния, что делает программу более интерактивной и гибкой.
### №5. 
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
### Ответ: 
```python
class Book:
    def __init__(self, title, author, year, genre):
        self._title = title
        self._author = author
        self._year = year
        self._genre = genre
        self._is_read = False

    def display_info(self):
        print(f"Название: {self._title}")
        print(f"Автор: {self._author}")
        print(f"Год издания: {self._year}")
        print(f"Жанр: {self._genre}")

    def mark_as_read(self):
        user_input = input(f"Прочитана ли книга '{self._title}'? (Да/Нет): ")
        if user_input.lower() == 'да':
            self._is_read = True
            print(f"Книга '{self._title}' отмечена как прочитанная.")
        elif user_input.lower() == 'нет':
            self._is_read = False
            print(f"Книга '{self._title}' отмечена как непрочитанная.")
        else:
            print("Некорректный ввод.")

class EBook(Book):
    def __init__(self, title, author, year, genre, file_size, file_format):
        super().__init__(title, author, year, genre)
        self.__file_size = file_size
        self.__file_format = file_format

    def display_info(self):
        super().display_info()
        print(f"Размер файла: {self.__file_size} МБ")
        print(f"Формат файла: {self.__file_format}")

class AudioBook(Book):
    def __init__(self, title, author, year, genre, duration, narrator):
        super().__init__(title, author, year, genre)
        self.__duration_minutes = duration * 60  # Длительность в минутах
        self.__narrator = narrator
        self.__listened_minutes = 0

    def display_info(self):
        super().display_info()
        print(f"Длительность: {self.__duration_minutes // 60} часов {self.__duration_minutes % 60} минут")
        print(f"Чтец: {self.__narrator}")
        print(f"Прослушано: {self.__listened_minutes // 60} часов {self.__listened_minutes % 60} минут")

    def mark_as_read(self):
        try:
            minutes = int(input(f"Сколько минут вы уже прослушали от книги '{self._title}'? "))
            if 0 <= minutes <= (self.__duration_minutes - self.__listened_minutes):
                self.__listened_minutes += minutes
                print(f"Обновлено: прослушано {self.__listened_minutes // 60} часов {self.__listened_minutes % 60} минут из {self.__duration_minutes // 60} часов.")
            else:
                print("Некорректное количество минут.")
        except ValueError:
            print("Некорректный ввод, введите целое число минут.")

# Создание объектов разных типов книг
ebook = EBook("Мастер и Маргарита", "Михаил Булгаков", 1966, "Роман", 2.5, "PDF")
audiobook = AudioBook("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 20, "Сергей Безруков")

# Полиморфный вызов метода display_info и интерактивное обновление статуса
for book in (ebook, audiobook):
    book.display_info()
    if isinstance(book, AudioBook):
        book.mark_as_read()
    else:
        book.mark_as_read()
    print()
```
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/s51.png)
![Меню](https://github.com/Alexsandra-Chunareva/Sasha-Chunareva/blob/tema8/скринs/s52.png)

### Вывод: 
Код представляет базовый класс `Book` и два его наследника `EBook` и `AudioBook`. У `AudioBook` добавлен метод `mark_as_read`, который позволяет пользователю вводить количество минут, уже прослушанных от аудиокниги, и сохранять прогресс. Программа демонстрирует полиморфизм, так как в цикле можно вызывать метод `mark_as_read` для объектов разного типа, вызывая соответствующий им результат.

# Общий вывод по теме:

Объектно-ориентированное программирование (ООП) — это передовая парадигма, которая организует код вокруг объектов, представляющих собой экземпляры классов. В основе ООП лежат несколько ключевых концепций:

1. **Классы и объекты**: Классы выступают в роли шаблонов для создания новых объектов, определяя их структуру и поведение.
2. **Атрибуты и методы**: Атрибуты представляют состояние объекта, а методы — его поведение.
3. **Наследование**: Позволяет создавать новые классы на основе уже существующих, что способствует повторному использованию кода и формированию иерархий классов.
4. **Инкапсуляция**: Обеспечивает сокрытие внутренних деталей реализации класса, предоставляя контролируемый доступ к его компонентам.
5. **Полиморфизм**: Позволяет объектам разных классов иметь общий интерфейс, но реагировать на одинаковые операции по-разному.

ООП играет ключевую роль в создании более модульного, гибкого и понятного кода. Оно позволяет разработчикам абстрагироваться от деталей реализации и сосредоточиться на моделировании объектов и их взаимодействии в программе. Такой подход улучшает структуру кода, облегчает его поддержку и расширение, а также способствует более эффективной организации сложных программных систем.
