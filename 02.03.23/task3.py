astr, bstr = input("Please, enter two numbers ").split()

a = int(astr)
b = int(bstr)

result = a%2==0 and b%2==0
print("Both numbers are even : " + str(result))

result = a%2==0 or b%2==0
print("At least one number is even : " + str(result))