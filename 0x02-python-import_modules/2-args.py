#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_count = len(argv) - 1

    print(args_count, "argument" + ("s" if args_count != 1 else "") + ":")

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
