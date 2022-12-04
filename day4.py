def sectionSplitter(assignment):
    ranges = assignment.split("-")
    bottomRange = int(ranges[0])
    topRange = int(ranges[1])
    sectionArrays = []
    for section in range(bottomRange, topRange+1):
        sectionArrays.append(section)
    return sectionArrays

# For part b...
def overlapChecker(array1, array2):
    completeOverlap = True
    for number in array2:
        if number not in array1:
            completeOverlap = False
    return completeOverlap


f = open("input.txt", "r")
content = f.readlines()
f.close()

amountOfCompleteOverlaps = 0
for line in content:
    line = line.replace("\n", "")
    formattedLine = line.split(",")
    elf1Assignment = sectionSplitter(formattedLine[0])
    print(elf1Assignment)
    elf2Assignment = sectionSplitter(formattedLine[1])
    print(elf2Assignment)

    if overlapChecker(elf1Assignment, elf2Assignment):
        amountOfCompleteOverlaps += 1
    else:
        if overlapChecker(elf2Assignment, elf1Assignment):
            amountOfCompleteOverlaps += 1
            
print(amountOfCompleteOverlaps)

# The working code I have
"""firstElfAssignment = [3, 4, 5, 6]
secndElfAssignment = [4, 5]

overlap = True
for assignedSection in secndElfAssignment:
    if assignedSection not in firstElfAssignment:
        overlap = False

print(overlap)"""


# go through the range and add each number to a list
# see if all numbers in one list are in the other
