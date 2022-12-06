def main():
    with open("input_d06.txt", "r") as f:
        buf = f.read().splitlines()

    print(f"Solution to part 1: {getmarkerpos(buf[0], 4)}")
    print(f"Solution to part 2: {getmarkerpos(buf[0], 14)}")

def getmarkerpos(string, rangetocheck):
    for i in range(rangetocheck-1, len(string)):
        if len(set(string[i-rangetocheck+1:i+1])) == rangetocheck:
            return i+1


if __name__ == "__main__":
    main()
