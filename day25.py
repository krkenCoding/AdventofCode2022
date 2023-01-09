# input.txt greatest line has 19 characters
# input2.txt greatest line has 6 characters

file = open("input.txt", "r")
content = file.readlines()

characterConvert = {"-": -1, "=": -2}
totalTotalSum = 0
for line in content:
    line = line.replace("\n", "")
    # Extend this dictionary to 19 keys once we switch to the proper input
    SNAFU2Decimal = {3814697265625: 0, 762939453125: 0, 152587890625: 0, 30517578125: 0, 6103515625: 0, 1220703125: 0, 244140625: 0, 48828125: 0, 9765625: 0, 1953125: 0, 390625: 0, 78125: 0, 15625: 0, 3125: 0, 625: 0, 125: 0, 25: 0, 5: 0, 1: 0}
    # We need to go backwards when it comes to reading the character and adding it to the SNAFU2Decimal dictionary
    for characterIndex in range(1, len(line)+1):
        # Finding the correct dictionary key to focus on
        dictionaryKey = list(SNAFU2Decimal)[-characterIndex]
        # Finding the right character to focus on from Test Input
        character = line[-characterIndex]

        # Turning the '-' and '=' into -1 and -2 respectively
        if character in characterConvert:
            character = characterConvert[character]

        # Adding the value into the dictionary
        SNAFU2Decimal[dictionaryKey] = int(character)

    totalSum = 0
    for key in SNAFU2Decimal:
        # Multiplying the key to the value then adding it to the sum
        totalSum += key*SNAFU2Decimal[key]
    totalTotalSum += totalSum

    print(SNAFU2Decimal, totalSum)

print("totalTotalSum", totalTotalSum)
