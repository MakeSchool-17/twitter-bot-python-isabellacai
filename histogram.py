import collections
import random

file = open('shirley.txt', 'r')

# makes a list of words in the file without all the punctuation
# text = [word.replace(",", "").replace(".", "").replace(";", "")
#         .replace(":", "") for line in file for word in line.lower().split()]


def create_histogram(source_text):
    c = collections.Counter()
    for a in source_text:
        c[a] += 1
    return c

    # [brian] You could also do:
    c.update(source_text)
    return c

def unique_words(histogram):
    # [brian] Nice!
    uniquewords = len(set(w.lower() for w in text))
    return uniquewords


def frequency(word, histogram):
    print(histogram[word])

# probability for each word

#
# def sumthing():
#     total = 0
#     for x in nums:
#         total += x
#     print(total)
#
# sumthing()


def total_words(histogram):
    total = 0
    for x in histogram:
        total += histogram[x]
    return total


def prob_word(word, histogram, words_amount):
    print(histogram[word]/words_amount)


def return_random_word(histogram):
    print(random.choice(list(create_histogram(text).keys())))


# print random.sample(create_histogram(source_text).keys())

if __name__ == '__main__':
    hist = create_histogram(text)

    # unique = unique_words(hist)

    totwords = total_words(hist)

    print(total_words(hist))

    print(unique_words(hist))

    frequency("us", hist)

    prob_word("us", hist, totwords)

    for word in hist:
        print(word, hist[word]/totwords)

    return_random_word(hist)
