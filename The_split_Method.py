family_members = "Grazyna, Krzysztof, Lukasz, Katarzyna, Zuzanna"
family_members_in_a_list = family_members.split(", ") #we're splitting the string based on a delimiter/separator which is a comma and a space
print(family_members_in_a_list) #returns a list with 5 elements

print(family_members.split(", ", 2)) #maxsplit is 2 so only 2 first elements are going to be splitted

sentence = "I really love some crispy tofu"
words = sentence.split(" ") #split based on a space
print(words)