import sys

try:
    # Get the input from the parameters
    input = int(sys.argv[1])
    option = int(sys.argv[2])

except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Your input is invalid!")
    sys.exit()


def double(x):
    return 2*x


def square(x):
    return x**2


def cube(x):
    return x**3


def doTwice(func, x):
    x = func(x)
    return func(x)


if option == 1:
    print(doTwice(double, input))
elif option == 2:
    print(doTwice(square, input))
elif option == 3:
    print(doTwice(cube, input))
else:
    print("It cannot be supported!")
    sys.exit()
