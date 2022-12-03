def main():
    with open("input_d03.txt", "r") as f:
        filecontents = f.read().splitlines()
    #filecontents = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nvv\ntt\nss".splitlines()
    part1(filecontents)
    part2(filecontents)

def part1(filecontents):
    commonlist = []

    for x in filecontents:
        commonlist.extend(commonitems(x))
    sum1 = 0
    for x in commonlist:
        sum1 += convchar(x)
    print(f"The solution of part 1: {sum1}")

def part2(filecontents):
    sum = 0
    for i in range (0,len(filecontents)//3):
        commonset = set({})
        for x in filecontents[(i*3)]:
            if x in filecontents[(i*3)+1] and x in filecontents[(i*3)+2]:
                commonset.add(x)
        for x in commonset:
            sum += convchar(x)
    print(f"The solution of part 2: {sum}")

def commonitems(rucksack):
    commonitems = set({})
    comp1 = rucksack[:(len(rucksack)//2)]
    comp2 = rucksack[(len(rucksack)//2):]
    for x in comp1:
        if x in comp2:
            commonitems.add(x)
    return commonitems

def convchar(char):
    priolist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, len(priolist)):
        if priolist[i] == char:
            return i+1


if __name__ == "__main__":
    main()




