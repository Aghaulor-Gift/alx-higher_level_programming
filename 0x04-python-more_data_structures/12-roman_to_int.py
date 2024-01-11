#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return None

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
    result = 0

    for char in roman_string:
        if char not in roman_numerals:
            return None

        value = roman_numerals[char]
        result += value

    return result
