import functools
import time


# Задача 1
def saved(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not cache.get(args):
            result = func(*args, **kwargs)
            cache[args] = result
            return result
        else:
            return cache[args]

    return wrapper


@saved
def multiplier(num):
    return num * 2


if __name__ == "__main__":
    print(multiplier(6))
    print(multiplier(6))


# Задача 2

def repeater(call_count=1, start_sleep_time=0.5, factor=2, border_sleep_time=10):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            sleep_time = start_sleep_time
            for counter in range(call_count):
                value = func(*args, **kwargs)
                if sleep_time < border_sleep_time:
                    sleep_time *= 2 ** factor
                    if sleep_time >= border_sleep_time:
                        sleep_time = border_sleep_time
                print(f'Запуск номер {counter + 1}. Ожидание:'
                      f' {sleep_time} секунд. Результат '
                      f'декорируемой функций = {value}')
                time.sleep(sleep_time)
            print('Конец работы')
        return wrapper
    return decorator


@repeater(4, 1, 2, 20)
def multiplier(num):
    return num * 2


if __name__ == "__main__":
    multiplier(2)
