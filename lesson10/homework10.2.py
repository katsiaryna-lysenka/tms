class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __iter__(self):
        return iter([self.name, self.age])

    @property
    def year_of_birth(self):
        return 2023 - self.age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name.lower() == other.name.lower() and self.age == other.age
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return False

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return False

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return False

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        return False


person1 = Person('Alex', 34)
# ==
assert person1 == Person('Alex', 34)
assert person1 == Person('alex', 34)
assert person1 == Person('ALEX', 34)
# !=
assert person1 != Person('Alex!', 34)
assert person1 != Person('Alex', 35)
# >
assert person1 > Person('Alex', 33)
assert person1 > Person('Ann', 33)
# <
assert person1 < Person('Alex', 35)
assert person1 < Person('Ann', 35)
# >=
assert person1 >= Person('Alex', 34)
assert person1 >= Person('Alex', 33)
assert person1 >= Person('Ann', 34)
assert person1 >= Person('Ann', 33)
# <=
assert person1 <= Person('Alex', 34)
assert person1 <= Person('Alex', 35)
assert person1 <= Person('Ann', 34)
assert person1 <= Person('Ann', 35)


