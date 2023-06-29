import random


class RandomValue:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return RandomValueIterator(self.limit)


class RandomValueIterator:

    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return random.randint(1, 100)
        else:
            print('Iterator is stopped!')
            raise StopIteration


my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None