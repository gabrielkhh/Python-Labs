import sys

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])

    average = (num1 + num2 + num3) / 3

    print('Average:%0.2f' % average)

except:
    print('Your input is invalid!')
