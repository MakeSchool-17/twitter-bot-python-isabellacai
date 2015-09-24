import collections
# input_file = open("shirley.txt")
#
# words = []
# for line in input_file:
#     words.append(word)
#
# def histogram(arg):
#     pass
#
# def unique_words(histogram, unique_words):
#     pass
#
# def frequency(word, histogram):
#     pass


file = open('shirley.txt', 'r')
text = [word.replace(",", "").replace(".", "").replace(";", "")
        .replace(":", "") for line in file for word in line.lower().split()]


print(text)
c = collections.Counter()
# with open('shirley.txt', 'r') as f:
#     for line in f:
#         for word in line.lower().line.strip(',').split():
#             word.replace(".", "")
#             words.append(word)
# print(words)

for a in text:
    c[a] += 1

print(c)
