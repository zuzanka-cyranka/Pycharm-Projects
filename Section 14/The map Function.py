#Functions in Python can be treated like any other data type
#For example, we can save a function in a list or pass a function as an argument in another function

#The map function accepts two arguments (1. a function and 2. an iterable object
#First, the map invokes the passed function on every element in the second passed iterable object

numbers = [8, 16, 24, 32, 40]
#we want to have cube of those numbers

cube = [number ** 3 for number in numbers]
print(cube)
#solution using the comprehension list

def cube(number):
    return number ** 3
print(map(cube, numbers)) #doesnt return anything, we have to specify that we want the result as a list
print(list(map(cube, numbers))) #now it returns the result in a list


animals = ["cat", "donkey", "mouse", "cricket"]
lengths = [len(animal) for animal in animals]
print(lengths)

def lengths(animal):
    return len(animal)
print(list(map(lengths, animals))) #we actually don't have to create a custom function, because:
print(list(map(len, animals))) #we are using len() function anyways!