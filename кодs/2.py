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