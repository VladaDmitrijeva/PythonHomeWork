def Swap_tuple(my_tuple: tuple):
    new_tuple = list(my_tuple)
    new_tuple[0], new_tuple[-1] = new_tuple[-1], new_tuple[0]
 
    return tuple(new_tuple)

print(Swap_tuple((2,3,4,5,9)))