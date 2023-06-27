from dataclasses import dataclass

@dataclass(frozen=True)
class MyDataClass:
    a: str
    b: int
    c: list

    @classmethod
    def build(cls, a, b, c):
        if isinstance(a, str) and isinstance(b, int) and isinstance(c, list):
            return cls(a, b, c)
        else:
            raise TypeError("Неверные типы для a, b или c")


person1 = MyDataClass.build("TEST", 34, [1, 2, 3])  # valid parameters
print(person1)
try:
    person2 = MyDataClass.build(100, 33, [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", "33", [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", 33, (1, 2, 3))  # invalid parameters
except Exception as exc:
    print(exc)
