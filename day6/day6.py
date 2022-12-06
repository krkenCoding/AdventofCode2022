# Part A
f = open("input.txt", "r")
content = f.readlines()
# content = ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]
index = 0
characterList = []

for line in content:
    # Go through every character in the line
    for character in line:
        # print("index:", index, character)
        # Add character to a list called characterList
        characterList.append(character)
        repeat = False
        # Go through 1->13, 14 iterations. Change the 14 to 4 to get the ans for part a 
        for nextCharactersIndex in range(1, 14):
            # newCharacter will be the next 14 characters one at a time
            newCharacter = line[index+nextCharactersIndex]
            # check if new character isn't already in the list
            if newCharacter not in characterList:
                # if it isn't then add it to the list
                characterList.append(newCharacter)
            # if new character is already in the list then...
            else:
                print("repeat found.")
                # reset the list
                characterList = []
                repeat = True
                break
            print(characterList)
        if repeat == False:
            # change it to + 3 to get ans to part a
            print(characterList, index + 14)
            quit()
        index += 1
