class Car:  # Определение класса 'Car'
    def __init__(self, make, model):  # Метод инициализации экземпляра класса
        self.make = make  # Присваивание значения параметра 'make' атрибуту 'make' объекта
        self.model = model  # Присваивание значения параметра 'model' атрибуту 'model' объекта

# Создание экземпляра класса 'Car' с параметрами 'Toyota' и 'Corolla'
my_car = Car("Toyota", "Corolla")
# Вывод информации об автомобиле на экран
print(f"Бренд: {my_car.make}, Модель: {my_car.model}")