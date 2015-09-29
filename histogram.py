import collections
import random

file = open('shirley.txt', 'r')

# makes a list of words in the file without all the punctuation
text = [word.replace(",", "").replace(".", "").replace(";", "")
        .replace(":", "") for line in file for word in line.lower().split()]


def create_histogram(source_text):
    c = collections.Counter()
    for a in source_text:
        c[a] += 1
    return c

create_histogram(text)


def unique_words(histogram):
    uniquewords = len(set(w.lower() for w in text))
    print(uniquewords)


def frequency(word, histogram):
    print(histogram[word])


def return_random_word(histogram):
    print(random.choice(list(create_histogram(text).keys())))

    # print random.sample(create_histogram(source_text).keys())

if __name__ == '__main__':
    hist = create_histogram(text)

    unique_words(hist)

    frequency("us", hist)

    return_random_word(hist)
