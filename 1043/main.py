class Triangle():
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
    
    def is_values_valid(self):
        a = abs(self.__b - self.__c) < self.__a < self.__b + self.__c
        b = abs(self.__a - self.__c) < self.__b < self.__a + self.__c
        c = abs(self.__a - self.__b) < self.__c < self.__a + self.__b

        return a and b and c

    def get_perimeter(self):
        return self.__a + self.__b + self.__c

class Trapeze():
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)

    def get_area(self):
        return ((self.__a + self.__b) * self.__c) / 2

segments = input().split(' ')
a = segments[0]
b = segments[1]
c = segments[2]


triangle = Triangle(a,b,c)
trapeze = Trapeze(a,b,c)

if triangle.is_values_valid():
    print(f"Perimetro = {triangle.get_perimeter()}")
else:
    print(f"Area = {trapeze.get_area()}")