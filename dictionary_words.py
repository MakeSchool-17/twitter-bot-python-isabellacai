import random

wordlist = []
#
input_file = open('words.txt', 'r')
#
#
# for line in input_file:
#     line.strip()
#     wordlist.append(line)
#
# print(wordlist)

# for line in input_file.readlines():
#     line.rstrip()
#     wordlist.append(line)
#
# print(wordlist)

# for line in input_file.readlines():
#     print(line, end="")

# for line.strip() in input_file:
#     wordlist.append(line)
#
# print(wordlist)

with open('words.txt') as temp_file:
    some_list = [line.rstrip('\n') for line in temp_file]

print(some_list)
