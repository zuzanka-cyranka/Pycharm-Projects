ice_cream = [
    ["Chocolate", "Vanilla", "Hazelnut"],
    ["Pineapple", "Strawberry"],
    ["Stroopwafel", "Caramel", "Coconut", "Straciatella"]
]
all_flavors = []
for flavor_pack in ice_cream:
    for flavor in flavor_pack:
        all_flavors.append(flavor)

print(all_flavors)