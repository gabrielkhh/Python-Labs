# Open the file in read mode
file_object = open("Lab2_testData.txt", "r")
data_list = file_object.readlines()
adjusted = []
keyword_list = []

for line in data_list:
    line = line[:-1]
    adjusted.append(line)

data_list = adjusted
adjusted = None

for data in data_list:
    temp_list  = [s for s in data.split(',')]
    for temp in temp_list:
        keyword_list.append(temp)

count_dict = {}

# Iterate through and process the input, character by character.
for keyword in keyword_list:
    if keyword in count_dict:
        # The key already exists
        # So we just need to increment the count for the already existing keyword in our dictionary
        count_dict[keyword] += 1
    else:
        # The key doesn't exist yet
        # This is the first time the current keyword is seen, add it as a key and 1 as a count.
        count_dict[keyword] = 1

# First we sort the dictionary by the keyword in ascending order
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

outF = open("top_5.txt", "w")

# We only want to print the up to the top 5 keywords hence val < 5, starting from 0.
while val < while_counter:
    key_string = sorted_by_value[val][0]
    count_string = str(sorted_by_value[val][1])
    one_result = key_string + ':' + count_string + ','
    result_string += one_result
    outF.write(one_result[:-1])
    outF.write("\n")
    val += 1

# Because I automatically added a comma to the end of every entry, let's remove the last comma from our result.
result_string = result_string[:-1]

outF.close()

print(result_string)
