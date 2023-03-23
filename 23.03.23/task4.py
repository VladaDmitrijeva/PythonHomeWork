# list1 = [2,6,8,7,9,13,12,17,18]
# for i in list1:
#     if i % 2 == 0:
#         print(i)

def evennumber(list):
    for i in list:
        if i % 2 == 0:
            print(i,end=" ")

evennumber([2,6,8,7,9,13,12,17,18,200])


