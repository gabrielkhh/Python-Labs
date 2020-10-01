import sys

try:
    # Get the input from the parameters..
    input_start_year = int(sys.argv[1])
    input_end_year = int(sys.argv[2])
except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Nice try, professor")
    sys.exit()

potential_leap_years_count = 0
first_divisor = 4
second_divisor = 100
start_is_century = False
end_is_century = False
start_could_be_leap = False
leap_years_list = []
string_result = ""

# Find the number of potential leap years (divisible by 4) including century years
if input_start_year % first_divisor == 0:
    if input_start_year % second_divisor == 0:
        start_is_century = True
    start_could_be_leap = True
    temp_a = int(input_start_year / first_divisor - 1)
else:
    temp_a = int(input_start_year / first_divisor)

if input_end_year % second_divisor == 0:
    # We know the end of the range is also a century year
    end_is_century = True

temp_b = int(input_end_year / first_divisor)
potential_leap_years_count = temp_b - temp_a

if start_is_century:
    # Start of range is century year
    current_year_check = input_start_year
    temp_counter = 0
    while temp_counter < potential_leap_years_count:
        # if (current_year_check % 4 == 0) and (current_year_check % 100 == 0):
        # Year is potentially leap year and is a century year
        if current_year_check % 100 == 0:
            if current_year_check % 400 == 0:
                # This century year is a leap year
                leap_years_list.append(current_year_check)
        else:
            # Not a century year but is a leap year
            leap_years_list.append(current_year_check)

        # Check the next leap year candidate (4 years later duh) and increase our counter
        current_year_check += 4
        temp_counter += 1
elif end_is_century:
    # End of range is century year
    current_year_check = input_end_year
    temp_counter = 0
    while temp_counter < potential_leap_years_count:
        if current_year_check % 100 == 0:
            if current_year_check % 400 == 0:
                # This century year is a leap year
                leap_years_list.append(current_year_check)
        else:
            # Not a century year but is a leap year
            leap_years_list.append(current_year_check)

        # Check the next leap year candidate (4 years earlier) and increase our counter
        current_year_check -= 4
        temp_counter += 1

    leap_years_list.sort()
else:
    # None of the start or end is a century year
    if start_could_be_leap:
        current_year_check = input_start_year
        internal_counter = 0
        while internal_counter < potential_leap_years_count:
            if current_year_check % 100 == 0:
                # We're looking at a century year
                if current_year_check % 400 == 0:
                    # Century year is leap year
                    leap_years_list.append(current_year_check)
            else:
                # We're not looking at a century year
                leap_years_list.append(current_year_check)

            current_year_check += 4
            internal_counter += 1
    else:
        # Starting year isn't leap year, find the closest next leap year in the range
        temp_num = int(input_start_year / 4)
        corrected_num = temp_num + 1
        earliest_leap_year = corrected_num * 4
        current_year_check = earliest_leap_year
        internal_counter = 0
        while internal_counter < potential_leap_years_count:
            if current_year_check % 100 == 0:
                # We're looking at a century year
                if current_year_check % 400 == 0:
                    # Century year is leap year
                    leap_years_list.append(current_year_check)
            else:
                # We're not looking at a century year
                leap_years_list.append(current_year_check)

            current_year_check += 4
            internal_counter += 1


string_part_one = "The number of Leap Years is " + str(len(leap_years_list)) + ", "
if len(leap_years_list) == 0:
    string_result = string_part_one + "there are no Leap Years."
else:
    string_result = string_part_one + "the Leap Years are"

for year in leap_years_list:
    string_result += " " + str(year) + ","

# Remove the last comma that's unnecessary
string_result = string_result[:-1]

# Finally, show the result to the user
print(string_result)
