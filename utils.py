import datetime


def logger(path_filename):  # Декоратор с параметром
    def _logger(some_function):  # Декоратор

        def plus_log(*args, **kwargs):
            datetime_call = datetime.datetime.now()
            result_some_function = some_function(*args, **kwargs)
            s = f'время: {datetime_call.strftime("%d.%m.%Y %H:%M")}; имя: {str(some_function).split()[1]}; ' \
                f'аргументы: {args_kwargs_(args, kwargs)} ; результат: {result_some_function} \n'
            with open(path_filename, 'a', encoding='utf-8') as f:
                f.write(s)
            return result_some_function  # новая функция возвращает свой результат

        return plus_log  # декоратор возвращает новую функцию. проброс result-а.
    return _logger


# Вспомогательная функция для вывода аргументов args, kwargs в одну строку, без скобок, через запятую
# применяется в функции logger
def args_kwargs_(args, kwargs):
    s = ''
    x = 0
    y = len(args)
    z = len(kwargs)
    if args:
        for item in args:
            x += 1
            if x < y or z > 0:
                s += f'{item}, '
            else:
                s += f'{item}'  # если элемент крайний, то запятую не ставим
    x = 0
    if kwargs:
        for k, v in kwargs.items():
            x += 1
            if x < z:
                s += f'{k}={v}, '
            else:
                s += f'{k}={v}'  # если элемент крайний, то запятую не ставим
    return s