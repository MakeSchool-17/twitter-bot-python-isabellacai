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


def unique_words(histogram):
    uniquewords = len(set(w.lower() for w in text))
    return uniquewords


def frequency(word, histogram):
    print(histogram[word])

# probability for each word


def prob_word(word, histogram, each_unique):
    print(histogram[word]/each_unique)


def return_random_word(histogram):
    print(random.choice(list(create_histogram(text).keys())))

    # print random.sample(create_histogram(source_text).keys())

if __name__ == '__main__':
    hist = create_histogram(text)

    unique = unique_words(hist)

    unique_words(hist)

    frequency("us", hist)

    prob_word("us", hist, unique)

    return_random_word(hist)
