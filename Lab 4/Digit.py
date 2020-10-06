import sys

try:
    # Get the input from the parameters
    input_number = int(sys.argv[1])
except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Your input is invalid!")
    sys.exit()


def digit(x):
    if x < 10:
        return 1
    elif x > 9:
        return digit(x / 10) + 1


def digit_iterative(x):
    count = 1
    while x >= 10:
        count += 1
        x /= 10
    return count

print("The number of digit(s) calculated by recursive is %d and by iterative is %d." % (digit(input_number), digit_iterative(input_number)))