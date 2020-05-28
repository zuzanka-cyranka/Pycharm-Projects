# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(list):
    result = []
    for nested_list in list:
        if len(nested_list) == 3:
            for element in nested_list:
                result.append(element)

    return "".join(result)

print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
