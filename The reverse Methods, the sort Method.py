vitamins = ["B12", "D", "A", "K"]
vitamins.reverse()
print(vitamins)

print(vitamins.reverse()) #returns None


temperature = [12, 16, 23, 31, 5, 9, -1]
temperature.sort()
print(temperature)
print(temperature.sort()) #returns None

vitamins.sort()
vitamins.reverse() #vitamins now in descending order
print(vitamins)

clothes = ["skirt", "Blouse", "anorak", "dress", "Shoes"]
clothes.sort()  #uppercase sorted before lowercase
print(clothes)

def title_clothes(clothes):
    new_clothes = []
    for element in clothes:
        upper_clothes = element.title()
        new_clothes.append(upper_clothes)
        new_clothes.sort()
    return new_clothes


print(title_clothes(clothes))

print(sorted(clothes))


units_of_measurement = ["miles", "meters", "yards"]
units_of_measurement = units_of_measurement.reverse()
print(units_of_measurement)

spices = ["paprika", "nutmeg", "ginger", "cinnamon", "turmeric"]
spices.append(["garlic", "berbere", "sansho"])
print(spices)

numbers = [1, 4, 5, 7, 9]
numbers[1:3] = [6, 8]
print(numbers)