
myNumber = 10

myString = 'string'

myList = [
    myNumber,
    myString
]

myDict = {
    'width': 1920,
    'height': 1080,
    'full-screen': False,
    'motion-blur': True
}


def add(arg1, arg2):
    return arg1 + arg2


class Car:
    def __init__(self):
        self.engine = 'V 8 750 hp'
        self.wheels = [
            1, 2, 3, 4
        ]
        self.pwd = 6
        self.speed = 0

    def go(self, newSpeed):
        self.speed = newSpeed

    def __str__(self):
        return "Car (speed: {speed})".format(speed=self.speed)


myCar = Car()
print myCar
myCar.go(500)
print myCar
