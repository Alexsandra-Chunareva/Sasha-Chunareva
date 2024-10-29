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