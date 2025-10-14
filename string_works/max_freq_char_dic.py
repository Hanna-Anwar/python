string = input("enter a string ").lower()

# char_count = {}

# for ch in set(string):
  
#     char_count[ch] = string.count(ch)

# print(char_count)

char_count = {}

for ch in string:

    if ch in char_count:

        char_count[ch]+=1

    else:

        char_count[ch] =1

print(char_count)


max_frequency = 0

max_frequency_dict= {}

for k,v in char_count.items():

    if v > max_frequency:

        max_frequency = v

        max_frequency_dict.clear()

        max_frequency_dict[k] = v

print(max_frequency_dict)

