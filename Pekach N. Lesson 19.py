# Lesson 19
## Task1

from typing import Iterable, Iterator


def with_index(iterable: Iterable, start: int = 0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


## Task 2

def in_range(start: int, end: int, step: int = 1) -> Iterator[int]:
    if step == 0:
        raise ValueError("step argument must not be zero")

    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step


## Task 3

class CustomIterable:

    def __init__(self, *args):
        self.data = list(args)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]


if __name__ == "__main__":
    print("Testing with_index:")
    for index, value in with_index(["a", "b", "c"], 1):
        print(index, value)

    print("\nTesting in_range:")
    for num in in_range(2, 10, 2):
        print(num)

    print("\nTesting CustomIterable:")
    custom_iter = CustomIterable(10, 20, 30, 40)
    for item in custom_iter:
        print(item)
    print("Index access:", custom_iter[2])