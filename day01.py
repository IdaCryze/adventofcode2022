
def main():
    f = open("input_d01.txt")
    elveslist = []
    counter = 0
    for x in f:
        if x != "\n":
            counter += int(x)
        else:
            elveslist.append(counter)
            counter = 0
    print(f"The elve with the most calories is: {elveslist.index(max(elveslist))} with {max(elveslist)} calories")

    #Part 2
    elveslist.sort()
    elveslist.reverse()
    counter = 0

    for i in range(0, 3):
        counter += elveslist[i]
    print(f"The top three elves are carrying {counter} calories in total.")

if __name__ == "__main__":
    main()
