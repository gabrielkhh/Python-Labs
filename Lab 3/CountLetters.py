import sys

try:
    # Get the input from the parameters
    input_data = str(sys.argv[1])
except ValueError:
    print("Your input is invalid!")
    sys.exit()
except IndexError:
    print("Your input is invalid!")
    sys.exit()


def letter_count(str):
    results_dict = {}
    for char in str:
        if char in results_dict:
            # The key already exists
            # So we just need to increment the count for the already existing character in our dictionary
            results_dict[char] += 1
        else:
            # The key doesn't exist yet
            # This is the first time the current char is seen, add its ASCII value as a key and 1 as a count.
            results_dict[char] = 1

    return results_dict


def double_count(str1, str2):
    results_dict = {}

    results_dict = letter_count(str1 + str2)

    return results_dict


def various_count(*str):
    input_list = str
    results_dict = {}
    for word in input_list:
        for char in word:
            if char in results_dict:
                # The key already exists
                # So we just need to increment the count for the already existing character in our dictionary
                results_dict[char] += 1
            else:
                # The key doesn't exist yet
                # This is the first time the current char is seen, add its ASCII value as a key and 1 as a count.
                results_dict[char] = 1

    return results_dict


input_data = input_data.replace(",", "")
output_dict = various_count(input_data)
length_of_dict = len(output_dict)

# First we sort the dictionary by the character in descending order
sorted_by_key = sorted(output_dict.items(), key=lambda x: x[0], reverse=True)

result_string = ""

for item in sorted_by_key:
    result_string += "%s:%d " % (item[0], item[1])

result_string = result_string[:-1]

print(result_string)
