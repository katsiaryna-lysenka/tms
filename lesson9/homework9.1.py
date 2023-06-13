import self as self
import time

class Auto:

    def __init__(self, brand, age, color='red', mark=0, weight=0):
        print(brand, age, color, mark, weight)
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    def birthday(self):
        example.age += 1
        print(example.age)

    def move(self):
        print('move')

    def stop(self):
        print('stop')


class Track(Auto):
    def __init__(self, max_load, brand, age, color='green', mark=15, weight=99):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load


    def move(self):
        #super().move()
        print('attention')
        print('move')


    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Car(Auto):
    def __init__(self, max_speed, brand, age, color='black', mark=9, weight=150):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self, max_speed):
        print('move')
        print(f'max speed is {max_speed}')

example = Auto('BMW', 54, 'black', 13, 76)
Auto.move(self)
Auto.stop(self)
Auto.birthday(self)

Track(32, 'Alfa_Romeo', 4)
Track.load(self)
Track.move(self)

Car.move(self, 150)
Car(130, 'Bentley', 5, 'red', 8, 200)
Car(170, 'Acura', 3)




