# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise

def is_long(list):
    if len(list) > 5:
        return True
    else:
        return False

print(is_long([1, 2, 3, 4, 5, 6]))

print([5, 4, 3] not in [5, 4, 3])