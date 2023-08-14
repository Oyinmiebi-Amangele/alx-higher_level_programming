#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    sums = 0

    for i in range(count):
        if i == 0:
            continue
        else:
            sums += int(argv[i])
    print(sums)
