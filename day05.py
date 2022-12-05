
def main():
    with open("input_d05.txt", "r") as f:
        filecontents = f.read().splitlines()
    #filecontents = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2".splitlines()

    extractedcontents1 = extractfile(filecontents)

    movedstack1 = executecommands(extractedcontents1[0], extractedcontents1[1])
    outputstring = ""
    for x in movedstack1:
        outputstring+=x[-1]
    print(f"The solution to part 1 is: {outputstring}")

    extractedcontents2 = extractfile(filecontents)

    movedstack2 = executecommands9001(extractedcontents2[0], extractedcontents2[1])
    outputstring = ""
    for x in movedstack2:
        outputstring+=x[-1]
    print(f"The solution to part 2 is: {outputstring}")

def extractfile(filecontents):
    stacks = [[]]
    commands = []
    for x in filecontents:
        if len(x) != 0 and x.strip()[0] == "[":
            lineextracted = extractstack(x)
            for i in range(0, len(lineextracted)):
                if (lineextracted[i] != " "):
                    while len(stacks) < i+1:
                        stacks.append([])
                    stacks[i].insert(0,lineextracted[i])
        if len(x) != 0 and x[:4] == "move":
            commands.append(extractinstruction(x))

    return (stacks, commands)

def executecommands9001(stacks, commands):
    #print(stacks)
    for x in commands:

        templist = []
        for i in range(0, x[0]):
            if len(stacks[x[1]-1]) > 0:
                templist.append(stacks[x[1]-1].pop())
        templist.reverse()
        stacks[x[2]-1].extend(templist)

    return stacks

def executecommands(stacks, commands):
    for x in commands:
        for i in range(0, x[0]):
            if len(stacks[x[1]-1]) > 0:
                stacks[x[2]-1].append(stacks[x[1]-1].pop())
    return stacks



def extractinstruction(string):
    l1 = string.split(" from ")
    l2 = l1[1].split(" to ")
    return (int(l1[0].replace("move ", "")), int(l2[0]), int(l2[1]))



def extractstack(string):
    lstack = []
    for i in range(len(string)//4+1):
        lstack.append(string[(i*4)+1])
    return lstack


if __name__ == "__main__":
    main()
