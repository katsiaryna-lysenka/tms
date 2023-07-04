import random

class RandomValue:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for _ in range(10):
            yield random.randint(self.start, self.end)

class RandomValueGenerator:
    def __init__(self, start, end):
        self.random_value = RandomValue(start, end)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self.random_value)
            if value % 2 == 0:
                return value