fruit = ["apple", "banana", "figs", "lime", "orange"]

for item in reversed(fruit):
    print(f"{item} has a total of {len(item)} characters.")


errands = ["wake up", "python", "food", "shop", "cook", "sleep"]

for index, errand in enumerate(errands):
    print(f"{errand} is number {index + 1} on my list")

for index, errand in enumerate(errands, 1):
    print(f"{errand} is number {index} on my list")