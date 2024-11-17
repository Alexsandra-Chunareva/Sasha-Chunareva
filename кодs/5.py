class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного включения')


@SiteChecker
def site():
    print('> Усердная работа сайта')


if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
