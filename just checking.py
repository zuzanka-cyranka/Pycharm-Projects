# Define an in_list function that accepts a list of strings and a separate string.

# Return the index where the string exists in the list. If the string does not exist, return -1.

# Do NOT use the find or index methods.

# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1


strings = ["enchanted", "sparks fly", "long live"]
def in_list(list, string):
    for index, item in enumerate(list):
        if item == string:
            return index
    return -1


print(in_list(strings, "long live"))


