# Define a smallest_number function  that accepts a list of numbers.

# It should return the smallest value in the list.

# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_value(numbers):
    for number in numbers:
        return min(numbers)
print(smallest_value([1,2,3]))

def smallest_value(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

print(smallest_value([1,2,3]))


# Define a function concatenate that accepts a list of strings.

# The function should return a concatenated string which consists of all list elements whose length is greater than 2 characters.

# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(strings):
    concatenated_word = ""
    for word in strings:
        if len(word) > 2:
            concatenated_word += word
    return concatenated_word

print(concatenate(["covid", "19", "virus"]))

# Write a function super_sum that accepts a list of strings.

# The function should sum the index positions of the first occurence of the letter “s” in each word.

# Not every word is guaranteed to have an “s”.

# Don’t use the sum keyword as it’s a built-in keyword.
#
# super_sum([]) => 0
# super_sum(["mustache"]) => 2
# super_sum(["mustache", "greatest"]) => 8
# super_sum(["mustache", "pessimist"]) => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum(strings):
    position = 0
    for word in strings:
        position += word.index("s")
    return position

print(super_sum(["mustache", "greatest", "almost"]))
