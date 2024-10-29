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

my_ebook = EBook("Мастер и Маргарита", "Михаил Булгаков", 1966, "Роман", 2.5, "PDF")

my_ebook.display_ebook_info()
my_ebook.mark_as_read()
my_ebook.set_file_format()


