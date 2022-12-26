def horizontalScout(scoutRow):
    treeCount = 0
    for neighbour in scoutRow:
        if neighbour < tree:
            treeCount += 1
        else:
            treeCount += 1
            return treeCount
    return treeCount


def verticalScout(lowRange, highRange, inv):
    treeCount = 0
    if inv == True:
        for lineIndex in range(highRange, lowRange-1, -1):
            cleanLine = content[lineIndex].replace("\n", "")
            if cleanLine[xPos] < tree:
                treeCount += 1
            else:
                treeCount += 1
                return treeCount
        return treeCount
    else:
        for lineIndex in range(lowRange, highRange):
            cleanLine = content[lineIndex].replace("\n", "")
            if cleanLine[xPos] < tree:
                treeCount += 1
            else:
                treeCount += 1
                return treeCount
        return treeCount


f = open("input.txt", "r")
content = f.readlines()

# first/last row of trees
firstLine = content[0].replace("\n", "")
lastLine = content[-1].replace("\n", "")

scenicScore = 1
mostScenic = 0
lineNumber = 0
for line in content:
    line = line.replace("\n", "")

    # Count all the trees in the first and last row
    if line == firstLine or line == lastLine:
        print(lineNumber, line)
        lineNumber += 1
        continue
    else:
        xPos = 0
        neighbours = []
        for tree in line:
            scenicScore = 1
            # Count all the trees at the start and end of the row
            if xPos == 0 or xPos == 4:
                xPos += 1
                continue
            elif tree == 0:
                xPos += 1
                continue
            else:
                # Count the left
                lineToCheck = line[:xPos]
                leftTrees = horizontalScout(lineToCheck[::-1])
                scenicScore *= leftTrees

                # Count the right
                rightTrees = horizontalScout(line[xPos + 1:])
                scenicScore *= rightTrees

                """if lineNumber == 2 and xPos == 35:
                    breakpoint()"""
                # Count the top
                topTrees = verticalScout(0, lineNumber-1, True)
                scenicScore *= topTrees

                # Count the bottom
                bottomTrees = verticalScout(lineNumber + 1, len(content), False)
                scenicScore *= bottomTrees

                """print("tree:", tree, "lineNumber:",lineNumber, "xPos:",xPos)
                print("leftTrees", leftTrees)
                print("rightTrees", rightTrees)
                print("topTrees", topTrees)
                print("bottomTrees", bottomTrees)
                print("scenicScore", scenicScore,"\n")"""

                if scenicScore > mostScenic:    mostScenic = scenicScore
                print(lineNumber, xPos, tree + ":" , leftTrees, rightTrees, topTrees, bottomTrees, scenicScore)
            xPos += 1
        print(lineNumber, line)
        lineNumber += 1

print("mostScenic", mostScenic)

