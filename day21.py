with open("input/iA21.txt") as f:
	lines = f.read().splitlines()

allergens = {}

for line in lines:
	ingredient, allergen = line.split(" (")
	ingredient = ingredient.split(" ")
	allergen = allergen[9:-1].split(", ")
	for i in range(len(allergen)):
		for j in range(len(ingredient)):
			if allergens.get(allergen[i]) == None:
				allergens[allergen[i]] = [ingredient[j]]
			else:
				if allergen[j] not in allergens[ingredient[i]]:
					allergens[allergen[i]] += [ingredient[j]]
