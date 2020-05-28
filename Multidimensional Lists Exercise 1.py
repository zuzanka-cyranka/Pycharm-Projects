# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0


def nested_sum(list):
    all_numbers = []
    for element in list:
        for number in element:
            all_numbers.append(number)
    return sum(all_numbers)

print(nested_sum([]))
