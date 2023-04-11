class Person:
    def __init__(self,name:str,age:int,address:str) -> None:
        self.name = name
        self.age = age
        self.address = address

    def get_into(self):
        return f'Persons name is  {self.name} \nhe/she is  {self.age} years old \nAddress is  {self.address}'
    
Person1 = Person("Miks", 23, "Kalku iela 7")
Person2 = Person("Agnese", 18, "Vartu iela 90")

print(Person1.get_into())
print(Person2.get_into())