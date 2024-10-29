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
