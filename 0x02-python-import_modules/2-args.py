#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(argv()) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}\n".format(i + 1, sys.argv[i + 1]))
