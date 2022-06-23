import itertools
from functools import reduce

# Задача №1
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# Задача №2
def int32_to_ip(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))


# Задача 3
def zeros(n):
    x = n // 5
    return x + zeros(x) if x else 0


# Задача 4
def bananas(s) -> set:
    result = set()

    for word_combi in itertools.combinations(range(len(s)), len(s) - 6):
        new_arg = list(s)

        for i in word_combi:
            new_arg[i] = '-'

        x = ''.join(new_arg)

        if x.replace('-', '') == 'banana':
            result.add(x)

    return result


# Задача 5
def count_find_num(primesL, limit):
    base = reduce((lambda a, b: a * b), primesL, 1)
    if base > limit:
        return []
    nums = [base]
    for i in primesL:
        for n in nums:
            num = n * i
            while (num <= limit) and (num not in nums):
                nums.append(num)
                num *= i

    return [len(nums), max(nums)]
