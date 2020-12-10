#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argcount = len(argv)

    sumnum = 0

    for i in range(1, argcount):
        sumnum += int(argv[i])

    print(sumnum)
