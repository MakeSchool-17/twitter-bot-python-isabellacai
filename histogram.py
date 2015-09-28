import collections

file = open('shirley.txt', 'r')

# makes a list of words in the file without all the punctuation
text = [word.replace(",", "").replace(".", "").replace(";", "")
        .replace(":", "") for line in file for word in line.lower().split()]


def histogram(source_text):
    c = collections.Counter()
    for a in text:
        c[a] += 1
    print(c)


def unique_words():
    uniquewords = len(set(w.lower() for w in text))
    print(uniquewords)


def frequency(word, histogram):
    pass

histogram(text)
unique_words()
#
# histogram_result = histogram()
# unique_words_result = unique_words()
#
# print(unique_words_result)

# def word_probability():
#     print("word probability: " + str(unique_words_result))

# word_probability()
