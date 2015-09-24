import collections


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


c = collections.Counter()

for a in text:
    c[a] += 1

print(c)

uniquewords = len(set(w.lower() for w in text))

print(uniquewords)
