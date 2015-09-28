import collections

file = open('shirley.txt', 'r')

# makes a list of words in the file without all the punctuation
text = [word.replace(",", "").replace(".", "").replace(";", "")
        .replace(":", "") for line in file for word in line.lower().split()]


def create_histogram(source_text):
    c = collections.Counter()
    for a in source_text:
        c[a] += 1
    return c


def unique_words(histogram):
    uniquewords = len(set(w.lower() for w in text))
    print(uniquewords)


def frequency(word, histogram):
    print(histogram[word])


if __name__ == '__main__':
    hist = create_histogram(text)

    unique_words(hist)

    frequency("us", hist)
# frequency(each_word, hist)
#
# histogram_result = histogram()
# unique_words_result = unique_words()
#
# print(unique_words_result)

# def word_probability():
#     print("word probability: " + str(unique_words_result))

# word_probability()
