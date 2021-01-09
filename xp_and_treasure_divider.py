import math

copper = float(input("How many copper pieces collected? "))
silver = float(input("How many silver pieces collected? "))
gold = float(input("How many gold pieces collected? "))
platinum = float(input("How many platinum pieces collected "))

coin_xp = copper / 100 + silver / 10 + gold + platinum * 5

char = int(input("How many main characters in the party?"))
retainer = int(input("How many retainers in the party?"))

char_xp = coin_xp / (char + retainer)
retainer_xp = char_xp / 2

print("Main characters receive " + str(char_xp) + " experience points.")
print("Retainers receive " + str(retainer_xp) + " experience points.")
