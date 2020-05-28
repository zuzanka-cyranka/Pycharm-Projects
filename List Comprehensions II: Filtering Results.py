monsters = [
    "Blue-Maned Lynel",
    "Golden Lynel",
    "Silver Lynel",
    "Lynel",
    "White-Maned Lynel",
    "Black Moblin",
    "Blue Moblin",
    "Cursed Moblin",
    "Golden Moblin",
    "Moblin",
    "Silver Moblin",
    "Stalmoblin"
]

golden_monsters = []

for monster_name in monsters:
    if "Golden" in monster_name:
        golden_monsters.append(monster_name)
print(golden_monsters)

golden_monsters = [monster_name for monster_name in monsters if "Golden" in monster_name]
#i want to take every single monster_name for every monster_name in my monsters list and append it to the new
#list "golden_monsters" if a monster_name has "Golden" in it
print(golden_monsters)

print([len(monster_name) for monster_name in monsters if "Golden" in monster_name])

print([monster_name.split("Golden ")[1] for monster_name in monsters if "Golden" in monster_name])