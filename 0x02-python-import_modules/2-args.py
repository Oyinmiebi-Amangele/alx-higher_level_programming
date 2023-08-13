#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print(f'{count} arguments.')
    elif count == 1:
        print(f'{count} argument:')
    else:
        print(f'{count} arguments:')

    for i in range(count + 1):
        if i == 0:
            continue
        else:
            print(f'{i}: {argv[i]}')
