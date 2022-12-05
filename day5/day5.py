# Unfortunately crates position/stack hard coded by hand
# Columns were then deleted from the input file

columnStacks = {"column1": ["R", "P", "C", "D", "B", "G"], "column2": ["H", "V", "G"],
        "column3": ["N", "S", "Q", "D", "J", "P", "M"], "column4": ["P", "S", "L", "G", "D", "C", "N", "M"],
        "column5": ["J", "B", "N", "C", "P", "F", "L", "S"], "column6": ["Q", "B", "D", "Z", "V", "G", "T", "S"],
        "column7": ["B", "Z", "M", "H", "F", "T", "Q"], "column8": ["C", "M", "D", "B", "F"],
        "column9": ["F", "C", "Q", "G"]}

f = open("input.txt", "r")
content = f.readlines()
f.close()
for line in content:
    line = line.replace("\n", "").split(" ")
    amountToMove = int(line[1])
    fromPosition = line[3]
    toPosition = line[5]

    # Part A
    """
    for i in range(int(amountToMove)):
        fromColumnFocus = "column" + fromPosition
        fromArrayFocus = columnStacks[fromColumnFocus]
        toColumnFocus = "column" + toPosition
        toArrayFocus = columnStacks[toColumnFocus]
        lastElement = fromArrayFocus[-1]
        fromArrayFocus.pop()
        toArrayFocus.append(lastElement)
    stackMessage = ""
    for key in columnStacks:
        columnFocus = columnStacks[key]
        stackMessage += columnFocus[-1]
    print(stackMessage)
        """

    # Part B
    fromColumnFocus = "column" + fromPosition
    fromArrayFocus = columnStacks[fromColumnFocus]

    print("old fromArray:", fromArrayFocus)
    movingStack = []
    for stack in range(amountToMove):
        positionInStack = amountToMove - stack
        movingStack.append(fromArrayFocus[-positionInStack])
        fromArrayFocus.pop(-positionInStack)
    print("new fromArray:", fromArrayFocus)
    print("movingStack:", movingStack)
    print("")

    toColumnFocus = "column" + toPosition
    toArrayFocus = columnStacks[toColumnFocus]
    toArrayFocus.extend(movingStack)

stackMessage = ""
for key in columnStacks:
    columnFocus = columnStacks[key]
    stackMessage += columnFocus[-1]

print(stackMessage)
