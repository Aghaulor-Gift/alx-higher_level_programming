#!/usr/bin/python3
""" Append Write File Module """

def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8)
    and returns the number of characters added.
    """
    
    with open(filename, mode='a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added

if __name__ == "__main__":
    filename = "file_append.txt"
    text = "This School is so cool!\n"
    characters_added_count = append_write(filename, text)
    print(characters_added_count)
