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
        if word[index] == "e" or word[index] == "l" or word[index] == "f":
            return check(word, index + 1)
        else:
            remainder = word[:index] + word[index + 1:]
            return check(remainder, index)
    else:
        return word


remaining_characters = check(input_string, 0)
is_elfish = True

if ("e" not in remaining_characters) and ("E" not in remaining_characters):
    is_elfish = False
if ("l" not in remaining_characters) and ("L" not in remaining_characters):
    is_elfish = False
if ("f" not in remaining_characters) and ("F" not in remaining_characters):
    is_elfish = False

if is_elfish:
    print("%s is one elfish word!" % input_string)
else:
    print("%s is not an elfish word!" % input_string)
