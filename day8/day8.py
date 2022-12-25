def horizontalScout(scoutRow):
    for neighbour in scoutRow:
        if neighbour >= tree:
            return 0
    return 1


def verticalScout(lowRange, highRange):
    for lineIndex in range(lowRange, highRange):
        cleanLine = content[lineIndex].replace("\n", "")
        if cleanLine[xPos] >= tree:
            return 0
    return 1


f = open("input.txt", "r")
content = f.readlines()

# first/last row of trees
firstLine = content[0].replace("\n", "")
lastLine = content[-1].replace("\n", "")
visibleTrees = 0

reason = ""
lineNumber = 0
for line in content:
    line = line.replace("\n", "")

    # Count all the trees in the first and last row
    if line == firstLine or line == lastLine:   visibleTrees += len(line)
    else:
        xPos = 0
        neighbours = []
        for tree in line:
            reason = 'null'
            '''if tree == "2" and xPos == 4:
                breakpoint()'''
            # Count all the trees at the start and end of the row
            if xPos == 0 or xPos == 98:
                visibleTrees += 1
                reason = "edge"
            elif tree == 0:
                visibleTrees = visibleTrees
            else:
                # Check the left
                if horizontalScout(line[:xPos]) == 1:
                    visibleTrees += 1
                    reason = "left"
                # Check the right
                elif horizontalScout(line[xPos+1:]) == 1:
                    visibleTrees += 1
                    reason = "right"

                elif verticalScout(0, lineNumber) == 1:
                    visibleTrees += 1
                    reason = "top"
                elif verticalScout(lineNumber + 1, len(content)) == 1:
                    visibleTrees += 1
                    reason = "bottom"
            #print("tree:", tree, reason)
            xPos += 1
    print(lineNumber, line, visibleTrees)
    lineNumber += 1


print("Visible Trees:", visibleTrees)
