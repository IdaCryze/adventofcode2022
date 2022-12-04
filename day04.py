import re
def main():
    with open("input_d04.txt", "r") as f:
        filecontents = f.read().splitlines()
    #filecontents ="2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8".splitlines()
    part1(filecontents)
    part2(filecontents)

def part1(filecontents):
    sum = 0
    for x in filecontents:
        if isIntervalContained(x):
            sum += 1
    print(f"The solution for part 1 is: {sum}")

def part2(filecontents):
    sum = 0
    for x in filecontents:
        if doIntervalsOverlap(x):
            sum += 1
    print(f"The solution for part 2 is: {sum}")

def doIntervalsOverlap(fileline):
    elves = re.split(",", fileline)
    if (getinterval(True, elves[0])) >= (getinterval(True, elves[1])) and (getinterval(True, elves[0])) <= (getinterval(False, elves[1])):
        return True
    elif (getinterval(True, elves[0])) <= (getinterval(True, elves[1])) and (getinterval(False, elves[0])) >= (getinterval(True, elves[1])):
        return True
    return False

def isIntervalContained(fileline):
    elves = re.split(",", fileline)

    if (getinterval(True, elves[0])) <= (getinterval(True, elves[1])) and (getinterval(False, elves[0])) >= (getinterval(False, elves[1])):
        return True
    elif (getinterval(True, elves[0])) >= (getinterval(True, elves[1])) and (getinterval(False, elves[0])) <= (getinterval(False, elves[1])):
        return True
    return False

def getinterval(islowerinterval, fullinterval):
    if islowerinterval:
        return int(re.split("-", fullinterval)[0])
    else:
        return int(re.split("-", fullinterval)[1])

if __name__ == "__main__":
    main()
