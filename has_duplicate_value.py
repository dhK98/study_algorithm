
def has_duplicate_value(array):
    existing_numbers = []
    for i in range(array.length):
        if existing_numbers[array[i]] == 1:
            return True
        else :
            existing_numbers[array[i]] = 1

    return False