# int
myNumber = 10

# float
myNumberFloat = 10.0147

# str
myString = 'this is a string'

# list
myList = [
    myNumber,
    myString
]

# dict
myDict = {
    'width': 800,
    'height': 600,
    'full-screen': True,
    'motion-blur': False
}

# function
def add(arg1, arg2):
    return arg1 + arg2

# class Car
class Car:
    def __init__(self):
        self.engine = 'V 6 750 hp'
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
