#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args_len = len(argv)
    sum_result = 0

    for i in range(1, args_len):
        sum_result += int(argv[i])

    print(sum_result)
