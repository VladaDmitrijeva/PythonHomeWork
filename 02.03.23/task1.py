
astr = input ("Please, enter your age ")
bstr = input ("Do you have driver license? Please, answer Yes or No ")
a = int(astr)
b = str(bstr)
c = "Yes" 
d = "yes"
result = a >= 18 and b == c or b == d
print("You are able to drive : " + str(result))