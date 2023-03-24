Mynumbers = [1,2,3,4,5,6,7,8,9,11]

def myfunc(numbers):
    myset = set()
    for i in numbers:
        if not i % 3 == 0:
            myset.add(i)
    return myset
    
print(myfunc(Mynumbers))

