import sys

# Get the input from the parameters..
input_numbers = str(sys.argv[1])

numbers_list = []
centered_average_list = []
even_numbers_count = 0
odd_numbers_count = 0
sum_even_numbers = 0
sum_odd_numbers = 0
total_sum_for_centered_average = 0
centered_average = 0
difference_big_small = 0

try:
    numbers_list = [int(s) for s in input_numbers.split(',')]
except ValueError:
    print("Please enter valid integers.")
    sys.exit()

# Sort the list by ascending order
numbers_list = sorted(numbers_list, reverse=False)

for number in numbers_list:
    if number % 2 == 0:
        # Number is even
        sum_even_numbers += number
        even_numbers_count += 1
    else:
        # Number is odd
        sum_odd_numbers += number
        odd_numbers_count += 1

# Calculate the difference between the biggest and smallest number
difference_big_small = numbers_list[len(numbers_list) - 1] - numbers_list[0]

if len(numbers_list) > 2:
    # Trim the first and last element of the list before counting centered average
    centered_average_list = numbers_list[1:]
    centered_average_list = centered_average_list[:-1]

    # Calculate the centered average
    for value in centered_average_list:
        total_sum_for_centered_average += value

    centered_average = total_sum_for_centered_average / len(centered_average_list)
elif 0 < len(numbers_list) < 3:
    # Calculate the centered average
    for value in numbers_list:
        total_sum_for_centered_average += value

    centered_average = total_sum_for_centered_average / len(numbers_list)

print("The sum of all even numbers is %d, the sum of all odd numbers is %d, the difference between the biggest and smallest number is %d, the total number of even numbers is %d, the total number of odd numbers is %d, the centered average is %d." % (sum_even_numbers, sum_odd_numbers, difference_big_small, even_numbers_count, odd_numbers_count, centered_average))
