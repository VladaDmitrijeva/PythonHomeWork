astr, bstr, cstr = input("Please, enter the day month year ").split()

a = int(astr)
b = int(bstr)
c = int(cstr)

result = a == 2 and b == 3 and c == 2023
print("Date valid : " + str(result))


