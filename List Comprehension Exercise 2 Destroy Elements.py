# Declare a function destroy_elements that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(list1, list2):
    result = [element for element in list1 if element not in list2]
    return result

print(destroy_elements([1, 2, 3], [4, 5]))


test = [1, 2, 3, 4]
print(test.index(4))