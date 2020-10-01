import sys
import myMath

numbers_list = []

try:
    # Get the input from the parameters..
    input_numbers = str(sys.argv[1])
    numbers_list = [int(s) for s in input_numbers.split(',')]
except IndexError:
    print("Your input is invalid!")
    sys.exit()
except ValueError:
    print("Your input is invalid!")
    sys.exit()

biggest_num = myMath.maximum(numbers_list)
smallest_num = myMath.minimum(numbers_list)
big_small_difference = myMath.subtraction(biggest_num, smallest_num)

summation_of_max_min = myMath.add(biggest_num, smallest_num)
sum_of_all_numbers = myMath.sumTotal(numbers_list)
count_even_numbers = myMath.evenNum(numbers_list)

if smallest_num < 5:
    numbers_list = myMath.clear(numbers_list)

print("The difference is:%d The summation is:%d The summation of all input is:%d The number of even numbers is:%d The values in the list are: %s" % (myMath.subtraction(biggest_num, smallest_num), myMath.add(biggest_num, smallest_num), sum_of_all_numbers, count_even_numbers, numbers_list))
