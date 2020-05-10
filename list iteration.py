# Define a sum_of_lengths function that accepts a list of strings.

# The function should return the sum of the string lengths.

# sum_of_lengths(["Hello", "Bob"]) => 8
# sum_of_lengths(["Nonsense"])     => 8
# sum_of_lengths(["Nonsense", "or", "confidence"]) => 20

def sum_of_lengths(list):
    total = 0
    for element in list:
        total += len(element)
    print(total)

sum_of_lengths(["Hello", "Bob"])

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# product([1, 2, 3]) => 6
# product([4, 5, 6, 7]) => 840
# product([10]) => 10


def product(list):
    total = 1
    for number in list:
        total = total * number
    return total


print(product([2, 3]))

