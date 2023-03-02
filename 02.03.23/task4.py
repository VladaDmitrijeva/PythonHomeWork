astr = input("Please, enter the year ")

a = int(astr)

result = (a%4==0 and not a%100==0) or a%400==0
print("Leap year : " + str(result))