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
