def NegativeValueException(Exception):
    pass
def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина больше 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '1234567890'
    check_name(name)