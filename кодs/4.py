def personal_info(name, age, company = 'unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Александра", 20)
personal_info(*tom)

bob = ("Саша", 20, "Yandex")
personal_info(*bob)