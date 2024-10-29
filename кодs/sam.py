class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")


# Создание объекта класса Book
my_book = Book("Мастер и Маргарита", "Михаил Булгаков", 1966)

# Вывод информации о книге
my_book.display_info()

