#####################################################################################################################
# Part 1
"""
f = open("input.txt", "r")
content = f.readlines()
f.close()

elfNumber = 1
calorieAmount = 0
greatestCalorieAmount = 0
mostLoadedElf = 0


for line in content:
    line = line.replace("\n", "")
    if line == "":
        print(str(elfNumber) + ":", calorieAmount)
        if calorieAmount > greatestCalorieAmount:
            print("^Greatest Calorie amount changed! (" + str(greatestCalorieAmount) + "->", str(calorieAmount)+")")
            greatestCalorieAmount = calorieAmount
            mostLoadedElf = elfNumber
        elfNumber += 1
        calorieAmount = 0
    else:
        calorieAmount += int(line)
print(mostLoadedElf)
"""

#####################################################################################################################
# Part 2

f = open("input.txt", "r")
content = f.readlines()
f.close()

elfNumber = 1
calorieAmount = 0

elfs = {}
for line in content:
    line = line.replace("\n", "")

    if line == "":
        elfs[elfNumber] = calorieAmount
        elfNumber += 1
        calorieAmount = 0
    else:
        calorieAmount += int(line)

print(elfs)
topElfs = sorted(elfs, key=elfs.get, reverse=True)[:3]

print(topElfs)

calorieSum = 0
for elf in topElfs:
    calorieSum += elfs[elf]

print(calorieSum)
