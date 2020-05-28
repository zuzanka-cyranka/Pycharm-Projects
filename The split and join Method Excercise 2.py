# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"]) => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"]) => "cat er pillar"
# cleanup(["", "", " "]) => ""

def cleanup(list):
    for element in list:
        if " " in list:
            list.remove(" ")
        elif "" in list:
            list.remove("")
    new_list = (" ".join(list))
    return new_list


print(cleanup(["cat", " ", "er", " ", " ", "","pillar"]))