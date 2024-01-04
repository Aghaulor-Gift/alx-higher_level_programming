#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_count = len(argv) - 1

    print("{:d} argument{}{}".format(args_count, "s" if args_count != 1 else "", ":" if args_count != 0 else "."))

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
