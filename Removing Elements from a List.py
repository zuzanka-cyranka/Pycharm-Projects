# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# delete_all([1, 3, 5], 3) => [1, 5]
# delete_all([5, 3, 5], 5) => [3]
# delete_all([4, 4, 4], 4) => []
# delete_all([4, 4, 4], 6) => [4, 4, 4]


# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#
# push_or_pop([10]) => [10]
# push_or_pop([10, 4]) => []
# push_or_pop([10, 20, 30]) => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]

def push_or_pop(list):
    new_list = []
    for number in list:
        if number > 5:
            new_list.append(number)
        elif number <= 5:
            new_list.pop()
    return new_list

print(push_or_pop([60, 20, 2, 330, 5, 87]))

def delete_all(list, target):
    while target in list:
        list.remove(target)
    return list

print(delete_all([4, 4, 4, 5, 6], 4))