numbers = [2, 4, 6, 8]
squares = [number ** 2 for number in numbers]
#square every number within numbers and save it in squares list
print(squares)

names = ["Zuzia", "Kasia", "Agatka"]
insult = [name + " to gowno" for name in names]
#to every name within names list add " to gowno" and save it in an insult list
print(insult)

rivers = ["Wisla", "Odra", "Warta"]
print([len(river) for river in rivers])
#print length of each river within the rivers list
#everything must be wrapped in square brackets!

expressions = ["kurwa", "kaczynski to chuj", "jebac pis"]
print([expression.upper() for expression in expressions])

decimals = [2.90, 4.89, 9.34, 124.325]
print([int(decimal) for decimal in decimals])

print("List comprehensions always generate a brand new list!")

string = "donut"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in string:
    print(alphabet.index(char))

print([alphabet.index(char, 1) for char in string])


for number in range(20):
    print(number / 2)

print([number / 2 for number in range(20)])