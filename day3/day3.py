# Part A
"""
f = open("input.txt", "r")
content = f.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pointSum = 0

for line in content:
    line = line.replace("\n", "")
    compartmentSize = int(len(line)/2)
    firstCompartment = line[:compartmentSize]
    secndCompartment = line[compartmentSize:]

    for character in firstCompartment:
        if character in secndCompartment:
            sharedItemType = character
            break

    index = 1
    for letter in alphabet:
        if sharedItemType == letter:
            points = index
            index = 1
            break
        else:
            index += 1

    pointSum += points

    print(sharedItemType, firstCompartment, secndCompartment, points)

print(pointSum)"""

# Part B

f = open("input.txt", "r")
content = f.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pointSum = 0

commonItemTypes = []
memberNumber = 1
index = 1
for line in content:
    line = line.replace("\n", "")
    if memberNumber == 1:
        # Populate the commonItemTypes with all of the new items that elf #1 has
        for character in line:
            # Only if the character hasn't already been added.
            if character not in commonItemTypes:
                commonItemTypes.append(character)
    else:
        # Going through the list of commonItemsTypes
        # For the life of me i cannot explain why letters get skipped in the for itemType loop.
        # Repeating the loop a few times seems to work.
        for i in range(0, 10):
            for itemType in commonItemTypes:
                # If the itemType isn't in the line
                if itemType not in line:
                    # Remove the item!
                    commonItemTypes.remove(itemType)
    print(memberNumber, line, commonItemTypes)
    # if 4th Elf, then we've completed a group.
    if memberNumber == 3:
        print("Group Complete!")
        # Show the commonItemTypes we've got
        sharedItem = commonItemTypes[0]
        for letter in alphabet:
            if sharedItem == letter:
                points = index
                pointSum += points
                index = 1
                break
            else:
                index += 1

        # Reset the member number and the commonItem Types
        memberNumber = 1
        commonItemTypes = []
        print("Shared Item:", sharedItem, points)
        print("New pointSum:", pointSum, "\n")
    else:
        memberNumber += 1

print(pointSum)
