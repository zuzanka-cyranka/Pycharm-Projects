# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# length_match(["cat", "dog", "kangaroo", "mouse"], 3)) => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)) => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4)) => 0
# length_match([], 5)) => 0

def length_match(list, integer):
    amount_strings = 0
    for item in list:
        if len(item) == integer:
            amount_strings += 1
    return amount_strings


print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# sum_from(1, 2)   # 1 + 2 => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5 => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8 => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12 => 42

def sum_from(int1, int2):
    total = 0
    for number in range(int1, int2):
        total = total + number
        if number > int2:
            break
    return total + int2

print(sum_from(9, 12))

# Declare a function same_index_values that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# same_values([1, 2, 3], [3, 2, 1]) => [1]
# same_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]) => [1, 3]

def same_index_values(list1, list2):
    index_position = []             #it's empty now, we will fill it up with matching indexes
    for indexx, item1 in enumerate(list1):   #we enumerate through list1
        if item1 == list2[item1]:#if item1 from the list1 is equal to an element with the same index position
                                #the first element in list1 is 1 and its index position is 0. then we check the second list. what is the item at the same index position. 0 in this case? oh, it's 3, so its not matching
            index_position.append(indexx)      #then append this index to out index_position variable
    return index_position

print(same_index_values([1,2,3], [3,2,1]))