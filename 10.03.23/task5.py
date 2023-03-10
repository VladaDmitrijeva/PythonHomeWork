number = int(input("Enter the prime number: "))

if number == 1 :
    print("It is not prime number, sorry")
for i in range(2,number):
    if number % i == 0:
        print("It is not prime number, sorry")
        break
    else :
        print("It is prime number, great!")
        break
  
    # while number % i == 0:
    #     number = input("It is not prime number, try again:")
    # if not number % i == 0:
    #     print("It is prime number, great!")
    #     break

