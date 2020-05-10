# Define an only_evens function that accepts a list of numbers.
#
# It should return a new list consisting of only the even numbers from the original list.
#
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5]) => []
# only_evens([])        => []

def only_evens(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
        else:
            continue
    return result

print(only_evens([23094803925823905, 239501734650913432, -3405812]))

# Define a long_strings function that accepts a list of strings.
#
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# long_strings(["Hello", "Goodbye", "Sam"] => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"] => []
# long_strings([] => []

def long_strings(strings):
    long_strings_list = []
    for word in strings:
        if len(word) >= 5:
            long_strings_list.append(word)
        else:
            continue
    return long_strings_list

print(long_strings(["12345", "123", "3248909098"]))