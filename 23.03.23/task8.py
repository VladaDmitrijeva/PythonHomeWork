
def evennumber(dictionary):
    dictionary1 = []
    for key in dictionary:
        if dictionary[key] % 2 == 0:
            dictionary1.append(key)
    return dictionary1


workinghours = {"monday" : 5, "wednesday" : 9, "friday": 2, "saturday" : 4, "sunday" : 8}
print(evennumber(workinghours))

