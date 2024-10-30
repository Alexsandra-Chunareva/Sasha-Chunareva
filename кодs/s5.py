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
        self.__duration_minutes = duration * 60  
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

ebook = EBook("Мастер и Маргарита", "Михаил Булгаков", 1966, "Роман", 2.5, "PDF")
audiobook = AudioBook("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 20, "Сергей Безруков")

for book in (ebook, audiobook):
    book.display_info()
    if isinstance(book, AudioBook):
        book.mark_as_read()
    else:
        book.mark_as_read()
    print()
