# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.
#
# word_lengths("Mary Poppins was a nanny") => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut") => [8, 5, 2, 5]

def word_lengths(string:str):
    new_string = string.split(" ")  #splits the string in list elements
    lengths = []
    for word in new_string:
        lengths.append(len(word))
    return lengths
print(word_lengths("Zuzanna Zahorska"))