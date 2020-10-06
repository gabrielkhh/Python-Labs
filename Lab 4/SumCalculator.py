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


def sum_recursive(x):
    if x == 1:
        return 1
    elif x > 1:
        return sum_recursive(x - 1) + x


def sum_iterative(x):
    sum = 0
    for num in range(x):
        sum += (num + 1)
    return sum

result_recursive = 0
result_iterative = 0

if input_number > 0:
    result_recursive = sum_recursive(input_number)
    result_iterative = sum_iterative(input_number)
else:
    print("Your input is invalid!")
    sys.exit()

print("The SUM value calculated by recursive is %d and by iterative is %d." % (result_recursive, result_iterative))
