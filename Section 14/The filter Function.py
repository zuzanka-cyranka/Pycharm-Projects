#The filter() function works similarly to the map() function
animals = ["elephant", "cheetah", "cat", "doggo", "monkey"]
#solution using a list comprehension below
#we want to save all animals longer than 5 in a new list
long_animals = [animal for animal in animals if len(animal) > 5]
print(long_animals)

def long_animals_function(animal):
    return len(animal) > 5  #boolean. Is it true? okay, save. is it false? okay, discard
print(list(filter(long_animals_function, animals))) #solution using the filter method.
#saved in a list using the list() method