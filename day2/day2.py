"""# Part 1
print("hello")

file = open("input.txt", "r")
content = file.readlines()
file.close()

points = 0

for line in content:
    line = line.replace("\n","")
    opponentInput = line[0]
    playersInput = line[2]

    guideTranslation = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}

    opponentChoice = guideTranslation[opponentInput]
    playersChoice = guideTranslation[playersInput]

    if playersChoice == "rock":
        points += 1
    elif playersChoice == "paper":
        points += 2
    else:
        points += 3

    if opponentChoice == playersChoice:
        print("draw")
        points += 3

    elif opponentChoice == "rock" and playersChoice == "paper":
        print("win")
        points += 6

    elif opponentChoice == "paper" and playersChoice == "scissors":
        print("win")
        points += 6

    elif opponentChoice == "scissors" and playersChoice == "rock":
        print("win")
        points += 6

print(points)
"""

# Part B

file = open("input.txt", "r")
content = file.readlines()
file.close()

opponentTranslation = {"A": "rock", "B": "paper", "C": "scissors"}
playerTranslation = {"X": "lose", "Y": "draw", "Z": "win"}
winningGuide = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
losingGuide = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
points = 0
for line in content:
    line = line.replace("\n", "")

    opponentInput = line[0]
    playerInput = line[2]
    opponentChoice = opponentTranslation[opponentInput]

    playerOutcome = playerTranslation[playerInput]

    if playerOutcome == "draw":
        print(playerInput, "draw")
        points += 3
        playersChoice = opponentChoice
        if playersChoice == "rock":
            points += 1
        elif playersChoice == "paper":
            points += 2
        else:
            points += 3

    elif playerOutcome == "win":
        print(playerInput, "win")
        points += 6
        playersChoice = winningGuide[opponentChoice]
        if playersChoice == "rock":
            points += 1
        elif playersChoice == "paper":
            points += 2
        else:
            points += 3

    else:
        print(playerInput, "lose")
        playersChoice = losingGuide[opponentChoice]
        if playersChoice == "rock":
            points += 1
        elif playersChoice == "paper":
            points += 2
        else:
            points += 3

print(points)
