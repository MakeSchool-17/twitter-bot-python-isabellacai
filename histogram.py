import collections

file = open('shirley.txt', 'r')
text = [word.replace(",", "").replace(".", "").replace(";", "")
        .replace(":", "") for line in file for word in line.lower().split()]


def histogram():
    c = collections.Counter()
    for a in text:
        c[a] += 1
    print(c)


def unique_words():
    uniquewords = len(set(w.lower() for w in text))
    print(uniquewords)


def frequency(word, histogram):
    pass

unique_words()
