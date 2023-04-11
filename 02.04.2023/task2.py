class Rectangle:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height

    def area(self):
        self.area = self.width * self.height
        return self.area
    
    def perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter
    
number1 = Rectangle(3,4)

print(f'Area of rectangle 1 is {number1.area()}')
    
print(f'Perimeter of rectangle 1 is {number1.perimeter()}')