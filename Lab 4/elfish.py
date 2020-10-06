import sys

try:
    # Get the input from the parameters
    input_string = str(sys.argv[1])
except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Your input is invalid!")
    sys.exit()

def check(word, index):
    if index < len(word):
        char = word[index]
        if char == "e" or char == "l" or char == "f" or char == "E" or char == "L" or char == "F":
            return check(word, index + 1)
        else:
            remainder = word[:index] + word[index + 1:]
            return check(remainder, index)
    else:
        contains_elf = True
        if ("e" not in word) and ("E" not in word):
            contains_elf = False
        if ("l" not in word) and ("L" not in word):
            contains_elf = False
        if ("f" not in word) and ("F" not in word):
            contains_elf = False

        return contains_elf


is_elfish = check(input_string, 0)

if is_elfish:
    print("%s is one elfish word!" % input_string)
else:
    print("%s is not an elfish word!" % input_string)
