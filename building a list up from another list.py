random_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    new_list = []
    for number in random_numbers:
        new_list.append(number ** 2)
    return new_list

print(squares(random_numbers))


current_age = [24, 60]

def ageing(age):
    new_age = []
    for age in current_age:
        new_age.append(age + 20) #returns your age in 20 years in case you're stoopid and can't count
    return new_age

print(ageing(current_age))

random_numbers = [4, 8, 15, 16, 23, 42]
def convert_to_floats(numbers):
    floating_numbers = []
    for number in numbers:
        floating_numbers.append(float(number))
    return floating_numbers

print(convert_to_floats(random_numbers))

def even_or_odd(numbers):
    even_or_odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_or_odd_list.append(True)
        else:
            even_or_odd_list.append(False)
    return even_or_odd_list

print(even_or_odd(random_numbers))
