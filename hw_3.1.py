from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


# Задача 1
class CyclicIterator:
    def __init__(self, obj):
        self.b = list(obj)
        self.i = 0

    def __iter__(self):
        self.a = self.b[self.i]
        return self

    def __next__(self):
        x = self.a
        if self.i < len(self.b) - 1:
            self.i += 1
            self.a = self.b[self.i]
        elif self.i == len(self.b) - 1:
            self.i = 0
            self.a = self.b[self.i]
        return x


if __name__ == "__main__":
    check_set = {7, 8, 9, 10}
    check_range = range(1, 15)
    check_tuple = (3, 4, 5, 6)
    check_list = [1, 2, 15, 0]
    check_frozenset = frozenset(check_set)
    check_time = CyclicIterator([check_list, check_tuple, check_range, check_frozenset])
    for cyclic_iterator in check_time:
        for _ in cyclic_iterator:
            print(_)


# Задача 2
@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        step_range: timedelta = timedelta(days=1)
        for season in self.dates:
            show_start: datetime = season[0]
            while show_start <= season[1]:
                yield str(show_start)
                show_start += step_range


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
