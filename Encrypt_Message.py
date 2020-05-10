# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
#
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""
#
# 1) we feed the function a custom string (e.g. "zuza")
# 2) the function checks the index positions of every character within this string based on the alphabet variable
# 3) now we have the index positions, the function must swipe them by 2 (so "z" is index position of 25, so it becomes 2)
# 4) the function returns a new string ("zuza" becomes " bwbc")


# encrypted_string.append(alphabet.index(char))   #returns index position of every character of our string and appends it to the encrypted_string list





def encrypt_message(string:str):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    encrypted_index = []
    encrypted_text = []
    result = ""
    for char in string:
        if char in alphabet:
            new_index = alphabet.index(char) + 2
            if new_index == 26:
                new_index = 0
            elif new_index == 27:
                new_index = 1
            encrypted_index.append(new_index)
            encrypted_text.append(alphabet[new_index])
    for element in encrypted_text:
        result = result + element #result += element
    return result


print(encrypt_message("zjebane kurwa"))

