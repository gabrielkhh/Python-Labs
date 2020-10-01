import sys

# Get the input from the parameters..
input_data = str(sys.argv[1])

# Convert all uppercase letters to lowercase
lower_case_input = input_data.casefold()

count_dict = {}

# Iterate through and process the input, character by character.
for character in lower_case_input:
    # Get the ASCII value of the character
    character_ASCII_value = ord(character)

    if character_ASCII_value in count_dict:
        # The key already exists
        # So we just need to increment the count for the already existing character in our dictionary
        count_dict[character_ASCII_value] += 1
    else:
        # The key doesn't exist yet
        # This is the first time the current char is seen, add its ASCII value as a key and 1 as a count.
        count_dict[character_ASCII_value] = 1

# First we sort the dictionary by the character in ascending order
sorted_by_key = dict(sorted(count_dict.items(), key=lambda x: x[0], reverse=False))

# Next we sort the dictionary by descending order based on count, so because the dictionary has previously been sorted
# by ascending order based on the key already, the program automatically will compute those with same count in ascending
# ASCII values.
sorted_by_value = sorted(sorted_by_key.items(), key=lambda x: x[1], reverse=True)

result_string = ""
val = 0
while_counter = 5

if len(sorted_by_value) < 5:
    while_counter = len(sorted_by_value)

# We only want to print the up to the top 5 characters hence val < 5, starting from 0.
while val < while_counter:
    key_string = chr(sorted_by_value[val][0])
    count_string = str(sorted_by_value[val][1])
    one_result = key_string + ':' + count_string + ','
    result_string += one_result
    val += 1

# Because I automatically added a comma to the end of every entry, let's remove the last comma from our result.
result_string = result_string[:-1]

print(result_string)
