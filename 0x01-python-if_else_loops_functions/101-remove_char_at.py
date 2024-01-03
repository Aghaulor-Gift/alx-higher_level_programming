#!/usr/bin/python3
def remove_char_at(str, n):
    if 0 <= n < len(str):
        return str[:n] + str[n+1:]
    else:
        return str

if __name__ == "__main__":
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))
