import sys

try:
    input_candidate = str(sys.argv[1])
    input_pattern = str(sys.argv[2])

    candidate_list = [int(s) for s in input_candidate.split(',')]
    pattern_list = [int(s) for s in input_pattern.split(',')]
except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Your input is invalid!")

first_int_pattern = pattern_list[0]
pattern_count = 0

for count, num in enumerate(candidate_list, 0):
    is_pattern = False
    if num == first_int_pattern:
        internal_count = count
        # Could be a possible pattern, time to loop through the pattern list completely to determine if a pattern
        # has been found
        for val in pattern_list:
            # Make sure we don't go out of range when comparing the values
            if internal_count < len(candidate_list):
                if val == candidate_list[internal_count]:
                    internal_count += 1
                    is_pattern = True
                else:
                    is_pattern = False
            else:
                is_pattern = False

        if is_pattern:
            pattern_count += 1


print("Pattern appears %d time!" % pattern_count)
