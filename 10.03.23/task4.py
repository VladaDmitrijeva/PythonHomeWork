number1, number2 = (input("Eneter two numbers ")).split()
operation = input("Enter operation ")
n1 = int(number1)
n2 = int(number2)
ouroperation = ("+","-","*","/","%")

while operation not in ouroperation:
    operation = input("Operation provided isn't valid, please,try again: ")
if operation == "+" :
    result1 = n1 + n2
    print(result1)
elif operation == "-" :
    result2 = n1 - n2
    print(result2)
elif operation == "*" :
    result3 = n1 * n2
    print(result3)
elif operation == "/" :
    result4 = n1 / n2
    print(result4)
else : 
    result5 = n1 % n2 
    print(result5)