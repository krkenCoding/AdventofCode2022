# Part 1
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
