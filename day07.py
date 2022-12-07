def main():
    with open ("input_d07.txt") as f:
        filecontents = f.read().splitlines()
    fstree = {}
    cwd = []
    for x in filecontents:
        lineparser(x, cwd, fstree)
    dirssize = calcdirssize(fstree, 100000)
    print(f"The solution to part 1 is: {dirssize[1]}")
    #print(findsizeofsmallestfolder(fstree, 70000000-dirssize[0]))


def lineparser(line: str, cwd: list, fstree: dict):
    if line[0] == "$":
        line = line.replace("$ ", "")
        splitline = line.split(" ")
        if splitline[0] == "cd":
            if splitline[1] == "..":
                cwd.pop()
            elif splitline[1] != "/":
                cwd.append(splitline[1])
    else:
        a = fstree
        for x in cwd:
            a = a[x]
        splitline = line.split(" ")
        if str(splitline[0]) == "dir":
            a.update({str(splitline[1]): {}})
        else:
            a.update({str(splitline[1]) : int(splitline[0])})

def findsizeofsmallestfolder(fstree:dict, minimumsize: int):
    print("foo")

# This only works if the file paths are unique
def calcdirssize(fstree:dict, foldersizelimit: int):
    cwdsizecounter = 0
    limitcounter = 0
    for x in fstree.keys():
        if type(fstree.get(x)) is int:
            cwdsizecounter += fstree.get(x)
        elif type(fstree.get(x)) is dict:
            subdir = calcdirssize(fstree.get(x), foldersizelimit)
            cwdsizecounter += subdir[0]
            limitcounter += subdir[1]

    if cwdsizecounter <= foldersizelimit:
        limitcounter += cwdsizecounter


    return (cwdsizecounter, limitcounter)

if __name__ == "__main__":
    main()