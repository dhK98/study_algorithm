# def greatest_number(array):
#     for i in array:
#         is_val_the_greatest = True
#         for j in array:
#             if j > i:
#                 is_val_the_greatest = False

#         if is_val_the_greatest:
#             return i

def greatest_number(array):
    max_value = None
    for value in array:
        if max_value == None:
            max_value = value
        elif max_value < value:
            max_value = value
    
    return max_value if max_value != None else 0

print(greatest_number([1,2,3,4,5,6,7]))
