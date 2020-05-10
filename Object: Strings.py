# print("Zuzanna", "Zahorska", sep="~", end="!")
#
# # print("Zuzanna", "Zahorska", sep="~", end="!") CTRL + /
# # print("Zuzanna", "Zahorska", sep="~", end="!")
# # print("Zuzanna", "Zahorska", sep="~", end="!")


#print(float("zupa"))
# print(type(str(69.96)))
# I want to express this value as a string. However, I also want to add
#
# - a dollar sign (​$​) in front of the amount
#
# - a space and the word “dollars” at the end
#
# The final result should be "$99.45 dollars".
#
# Write the code to make this happen.
#
# NOTE: Your answer must use concatenation.
#
# NOTE: 99.45 must start out as a floating-point value. You cannot use "99.45". Instead, figure out a way to convert 99.45 to a string.

# number1 = input("Please insert a number: ")
# number2 = input("Please insert a second number: ")
# print("A sum of both numbers is: ", int(number1) + int(number2))
#or number1 = int(number1)
#or number1 = int(input("blabla"))

# print("My extraordinary program will help you EASILY convert Fahrenheit to Celsius!")
# user_input = float(input("Enter the temperature in Fahrenheit that you want to convert: "))
# celsius = (user_input - 32) * 5/9
# print(user_input, " Fahrenheid is ", celsius, "Celsius")
#
# print(days_remaining / 10)


# def easy_money():
#     return 180
#
# print(easy_money())
#
#
# def best_food_ever():
#     return "Sushi"
#
#
# print(best_food_ever())
#
#
# def convert_to_currency(currency):
#     return "$" + str(currency)


# print(convert_to_currency(15))

# def word_multiplier(word:str, times:int)->str:
#     return word*times
# print(word_multiplier("dog", 5))

# def product(a, b):
#     return a * b
#
#
# product(10, a=5)


# def product(a, b):
#     return a * b
#
#
# product(a=5)

# def long_word(a:str):
#     return len(a) >= 7
#
# print(long_word("zuzanna"))

# Define a first_longer_than_second function that accepts two string arguments.
# The function should return a True if the first string is longer than the second
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")   => True
# first_longer_than_second("cat", "mouse")     => False
# first_longer_than_second("Steven", "Seagal") => False

# def skjdk(first_string:str, second_string:str):
#     return len(first_string) > len(second_string) #is first_string longer than secon_string? if yes, return True
#
# print(skjdk("zuzanna", "duba"))
# print

# Define a same_first_and_last_letter function that accepts a string as an argument.
# The function should return a True if the first and last character are equal, and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner") => True
# same_first_and_last_letter("Runner") => False
# same_first_and_last_letter("clock")  => False
# same_first_and_last_letter("q")      => True

# def same_first_and_last_letter(string:str):
#     return string[0] == string[-1]
#
# print(same_first_and_last_letter("runner"))

# Define a three_number_sum function that accepts a 3-character string as an argument.
# The function should add up the sum of the digits of the string.
# HINT: You’ll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123") => 6
# three_number_sum("567") => 18
# three_number_sum("444") => 12
# three_number_sum("000") => 0
# import functools
# def three_number_sum(digid:str):
#     return functools.reduce(lambda a,v: a + v, [int(v) for v in digid])
#     #return int(digid[0]) + int(digid[1]) + int(digid[2])
#
# print(three_number_sum())

# address = "Middachtenstraat 347, 6535LP Nijmegen, Gelderland"
# print(address[-10: ])
#
# print("mastodon"[-5::2])

# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty") => "dyn"
# first_three_characters("empire")  => "emp"



# Define a last_five_characters function that accepts a string argument.
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty") => "nasty"
# last_fiee_characters("empire") => "mpire"

# def last_five_characters(string:str):
#     return string[-5:]
#
# print(last_five_characters("123456789"))

# Define a is_palindrome function that accepts a string argument.
# The function should return True if the string is spelled
# the same backwards as it is forwards.
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar") => True
# is_palindrome("yummy")   => False

# def is_palindrome(string:str):
#     return string[::1] == string[::-1]
#
# print(is_palindrome("nukun"))

# str1 = "Just a piece of string"
# print(str1.rfind("z"))

# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.

# def vowel_count(word:str):
#     return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
#
# print(vowel_count("Zanepious"))

# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#

# def find_my_letter(word:str, character:str):
#     return word.find(character)
#
# print(find_my_letter("pieter", "t"))

# website = "www.google.com"
# print(website.strip("com."))

# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ") => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ") => "nonsense"
# fancy_cleanup("grade") => "zrade"

# def fancy_cleanup(input:str):
#     return input.strip().replace("g", "z").replace(" ", "!")
#
# print(fancy_cleanup("       geronimo crikey  "))

# mad_libs = "{name} took a picture of a {adjective} {noun}."
# name = input("Enter a name: ")
# adjective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# print(mad_libs.format(name = name, adjective = adjective, noun = noun))

# name = "Zuza"
# adjective = "stinky"
# noun = "hobo"
# mad_libs = f"{name} laughed at the {adjective} {noun}."
# print(mad_libs)
#
#
# name = input("Enter a name: ")
# adjective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# mad_libs = f"{name} took a picture of a {adjective} {noun}."
# print(mad_libs)

# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string “even”.
# If the integer is odd, the function should return the string “odd”.
#
# even_or_odd(2) => "even"
# even_or_odd(0) => "even"
# even_or_odd(13) => "odd"
# even_or_odd(9) => "odd"

# def even_or_odd(number:int):
#     if number % 2 == 0:
#         return "even"
#     return "odd"
#
# print(even_or_odd(23874928373))

# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is ______"
# where the first space is the argument and the second space
# is either truthy or falsy.
#
# truthy_or_falsy(0) => "The value 0 is falsy"
# truthy_or_falsy(5) => "The value 5 is truthy"
# truthy_or_falsy("Hello") => "The value Hello is truthy"
# truthy_or_falsy("") => "The value  is falsy"

# def truthy_or_falsy(input):
#     if input == 0 or input == "":
#         return f"The value {input} is falsy"
#     return f"The value {input} is truthy"
#
# print(truthy_or_falsy(None))
#
# print(bool(5))


# value = None
# if value:
#     print(f"{value} is truthy")
# else:
#     print("falsy")

# Define an up_and_down function that accepts a string argument
# If the string consists of all uppercase letters, return a new string
# consisting of all lowercase letters. If the string consists of all
# lowercase letters, return a new string consisting of all uppercase
# characters. If the string has a mix of uppercase and lowercase
# characters, return a new string where the casing of each letter is swapped.
#
# up_and_down("HELLO") => "hello"
# up_and_down("genius") => "GENIUS"
# up_and_down("ESPreSso") => "espREsSO"

# def up_and_down(word:str):
#     if word.isupper():
#         return word.lower()
#     elif word.islower():
#         return word.upper()
#     else:
#         return word.swapcase()
#
#
# print(up_and_down("ESPreSso"))

# Declare a negative_energy function that accepts a numeric argument and returns its absolute value.
# The absolute value is the number's distance from zero.
#
# negative_energy(5) => 5
# negative_energy(10) => 10
# negative_energy(-5) => 5
# negative_energy(-8) => 8
# negative_energy(0) => 0

# def negative_energy(number):
#     return abs(number)
#
# print(negative_energy(0))
#
# def negative_energy(number):
#     if number >= 0:
#         return number
#     elif number < 0:
#         return -number
#
# print(negative_energy(0))

# name = "zUzanna"
# #
# # if name.istitle():
# #     proper_name = "It's a valid name"
# # else:
# #     proper_name = "Invalid"
# #
# # print(proper_name)
# #
# # proper_name = "It's a valid name" if name.istitle() else "Invalid name"
# # print(proper_name)

##vegan dish!
#the program gives you recommendation for today's dinner based on ingredients you already have
#same program, two approaches
# ingredient1 = "Tofu"
# ingredient2 = "Soy sauce"
#
# if ingredient1 == "Tofu" and ingredient2 == "Soy sauce":
#     print("Fried tofu with some soy sauce!")
# elif ingredient1 == "Tofu":
#     print("Plain tofu is always nice!")
# else:
#     print("You need to do some groceries.")
#
# if ingredient1 == "Tofu":
#     if ingredient2 == "Soy sauce":
#         print("Fried tofu with some soy sauce!")
#     else:
#         print("Plain tofu is always nice!")
# else:
#     print("You need to do some groceries!")

# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4 . It should return False otherwise.

# divisible_by_three_and_four(3) => False
# divisible_by_three_and_four(4) => False
# divisible_by_three_and_four(12) => True
# divisible_by_three_and_four(18) => False
# divisible_by_three_and_four(24) => true
#
# def divisible_by_three_and_four(number):
#     if number % 3 == 0 and number % 4 == 0:
#         return True
#     else:
#         return False

# print(divisible_by_three_and_four(24))

# Declare a string_theory function that accepts a string as an argument.

# It should return True if the string has more than 3 characters and starts with a capital “S”. It should return False otherwise.

# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

# def string_theory(word:str):
#     if len(word) > 3 and word[0] == "S":
#         return True
#     else:
#         return False
#
# print(string_theory("Sniper"))

# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# invalid_number = True #we set invalid_number to True so our while loop can execute (we assume the user is dumb)
#
# while invalid_number: #keep repeating the code; this line evaluates to True
#     user_value = int(input("Enter a number greater than 10: ")) #we ask the dumbo to provide a valid number
#     if user_value > 10: #if the dumbo provides a valid number, the rest of the code wll be executed. if not
#         #the while loop will continue until we get a number greater than 10
#         print(f"Thanks, {user_value} is a great choice!") #we got a valid number
#         invalid_number = False #we change the variable invalid_number to False to break the loop. otherwise, it will
#         #become an infite loop


# def fizzbuzz(number:int):
#     count = 0               #nasz poczatkowy licznik
#     while count < number:   #program ma dzialac tak dlugo, jak licznik bedzie mniejszy niz numer podany przy funkcji
#         count +=1           #przy kazdym nowym uruchomieniu loopa, do licznika dodajemy 1 (w ten sposob idziemy od 0 w gore)
#         if count % 3 == 0 and count % 5 == 0:
#             print("FizzBuzz")
#         elif count % 3 == 0:
#             print("Fizz")
#         elif count % 5 == 0:
#             print("Buzz")
#         else:
#             print(count)
#
#
# fizzbuzz(2137)

#counts down from number to 0

# def count_down(number):
#     while number > 0:
#         print(number)
#         number -= 1
# count_down(-9)
#
# def count_down_from(number):
#     if number <= 0:
#         return
#     else:
#         print(number)
#         count_down_from(number - 1)
#
#
# count_down_from(5)
# def reverse(string:str):
#     while string:
#         string_length = len(string)
#         new_string = string[string_length::-1]
#         return new_string
#
# print(reverse("jan pawel drugi jebany pedofil"))
#
# def reverse(string:str):
#      if len(string) <= 1:
#          return string
#      else:
#          string_length = len(string)
#          new_string = string[string_length::-1]
#          reverse(new_string)
#
# print(reverse("Zuzanna"))


print("zuzanna"[0:5])

animals = ["dog", "cat", "salmon", "cow"]
for animal in animals:
    print(len(animal))


numbers = [1,2,5,8,10]
total = 0
for number in numbers:
    total = total + number

print(total)