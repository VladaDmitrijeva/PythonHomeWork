class Car:
    def __init__(self,make:str,model:str,year:str) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return "Make : " + self.make + "\nModel : " + self.model + "\nYear : " + self.year

myCar1 = Car("Kia", "Rio", "2019")
myCar2 = Car("Honda", "Civic", "2008")

print(myCar1.get_info())
print(myCar2.get_info())