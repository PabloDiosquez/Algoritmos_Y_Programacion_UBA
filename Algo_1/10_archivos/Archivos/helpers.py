# This function gets lines from a file given its path
def get_lines(path):
    with open(path, 'r', encoding='UTF-8') as file:  # Opens the file in read mode using UTF-8 encoding
        return [line.strip() for line in file.readlines()]  # Strips each line in the file and returns a list

# This function writes lines to a file specified by its path
def set_file(path: str, lines: list):
    try:
        with open(path, 'w', encoding='UTF-8') as file:  # Opens the file in write mode using UTF-8 encoding
            file.writelines(lines)  # Writes the lines to the file
        print("File successfully created!")  # Message indicating successful file creation
    except:
        raise Exception("Error")  # Raises an exception in case of an error

# This function zips two lists together into a list of tuples
def zipB(listA, listB):
    if is_empty(listA) or is_empty(listB): return []  # Checks if either list is empty, if so, returns an empty list
    return [(listA[0], listB[0])] + zipB(listA[1:], listB[1:])  # Zips the lists into a list of tuples

# This function checks if a list is empty
def is_empty(listA):
    return not len(listA)  # Returns True if the length of the list is zero, indicating it's empty