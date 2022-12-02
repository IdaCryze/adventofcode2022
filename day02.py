import re
def main():
    f = open("input_d02.txt")
    counter = 0
    for x in f:
        if re.search("[A-C] [X-Z]", str(x)) is not None:
            counter += calcscore1(convchars(x[0:len(x)-1]))
    print(f"Solution #1: {counter}")
    counter = 0
    f = open("input_d02.txt")
    for x in f:
        if re.search("[A-C] [X-Z]", str(x)) is not None:
            counter += calcscore2(convchars(x[0:len(x)-1]))

    print(f"Solution #2: {counter}")

#allows me to perform arithmetic operations in place of dumb comparisons
def convchars(string):
    listrps = re.split(" ", string)
    listint = [0,0]

    if listrps[0] == "A":
        listint[0] = 0
    elif listrps[0] == "B":
        listint[0] = 1
    elif listrps[0] == "C":
        listint[0] = 2

    if listrps[1] == "X":
        listint[1] = 0
    elif listrps[1] == "Y":
        listint[1] = 1
    elif listrps[1] == "Z":
        listint[1] = 2

    return listint

def weirdAdder(x,y):
    retVal = x+y
    if retVal < 0:
        retVal = 2
    elif retVal > 2:
        retVal = 0
    return retVal

def isWin1(x,y):
    if y-x==1:
        return True
    elif x==2 and y==0:
        return True
    else:
        return False

def calcscore1(intlist):
    counter = 0
    counter += intlist[1]+1

    if intlist[0] == intlist[1]:
        counter += 3
    elif isWin1(intlist[0], intlist[1]):
        counter += 6

    return counter

def calcscore2(intlist):
    retVal = 0
    if intlist[1] == 0:
        retVal = calcscore1([intlist[0], weirdAdder(intlist[0], -1)])
    elif intlist[1] == 1:
        retVal = calcscore1([intlist[0], intlist[0]])
    elif intlist[1] == 2:
        retVal = calcscore1([intlist[0], weirdAdder(intlist[0], 1)])
    return retVal

if __name__ == "__main__":
    main()
