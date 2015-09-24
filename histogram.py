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

words = []

with open('shirley.txt', 'r') as f:
    for line in f:
        for word in line.strip(',').split():
            words.append(word)


print(words)
