list = [8,3,6,1,3,1,1]
# list.sort()
# print(list)

list_sorted = []

while list:
    minnumber = min(list)
    list_sorted.append(minnumber)
    list.remove(minnumber)

print(list_sorted)

