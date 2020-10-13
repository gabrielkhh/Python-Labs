import sys
from functools import reduce

try:
    # Get the input from the parameters
    input_numbers = str(sys.argv[1])
    sales_list = [int(s) for s in input_numbers.split(',')]
    scale_factor = int(sys.argv[2])

except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Your input is invalid!")
    sys.exit()


def scale(list1, x):
    return list(map(lambda y: y * x, list1))


def sort(list1):
    return sorted(list1, key=lambda x: x % 10)


def goodSales(list1):
    total_sum = reduce(lambda a,b: a + b, list1)
    return list(filter(lambda c: ((c > (total_sum/len(list1))) is True), list1))


print("The scaled number is: %a The sorted sales numbers are: %a The good sales numbers are: %a" % (scale(sales_list, scale_factor), sorted(sales_list), goodSales(sales_list)))
