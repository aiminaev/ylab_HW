import functools
import time


# Задача 1
# def saved(func):
#     cache = {}
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if not cache.get(args):
#             result = func(*args, **kwargs)
#             cache[args] = result
#             return result
#         else:
#             return cache[args]
#
#     return wrapper
#
#
# @saved
# def multiplier(num):
#     return num * 2
#
#
# if __name__ == "__main__":
#     print(multiplier(6))
#     print(multiplier(6))


# Задача 2

def try_repeat(call_count, start_sleep_time, factor, border_sleep_time):
    def inner(func):

        def wrapper(*args, **kwargs):
            nonlocal call_count, start_sleep_time
            for number in range(1, call_count + 1):
                time.sleep(start_sleep_time)
                result = func(*args, **kwargs)
                print(f'Запуск номер {number}. '
                      f'Ожидание: {start_sleep_time} сек. '
                      f'Результат декорируемой функций = {result}')
                start_sleep_time *= factor
                if border_sleep_time <= start_sleep_time:
                    start_sleep_time = border_sleep_time
            print('Конец работы')

        return wrapper

    return inner

@try_repeat(4,1,2,20)
def multiplier(num):
    return num * 2

print(multiplier(2))