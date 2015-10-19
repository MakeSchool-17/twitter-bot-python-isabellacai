# [brian] Careful! This file uses tabs to indent the code. In python this is a
# pretty bad idea. It seems like a pretty small thing, and it is, but you can
# also indent your code using spaces, and having both methods is confusing and
# a little inefficient.

# The python community had decided to stick with spaces, the rest of your code
# follows conventions pretty perfectly though. The names are all great and you're
# adding whitespace in all the right places, it looks like the code of a pro!
import random
from collections import defaultdict # [brian] Explained below
import markovgen


class Markov(object):

    def __init__(self, open_file):
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()

    def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words

    def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""

		# [brian] You don't need this guard, the range() will return an empty
		# sequence, and the function will return on its own.
		if len(self.words) < 3:
			return

		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]

		# [brian] The above code uses a really common pattern in python, checking if a key
		# exists, and if it doesn't using a default value for the key. Python includes
		# defaultdict to make writing this code easier for you. The above code could be
		# written:

		self.cache = defaultdict(list)

		for w1, w2, w3 in self.triples():
			self.cache[(w1, w2)].append(w3)

		# defaultdict takes a constructor, and when the key isn't found calls that
		# constructor instead of throwing an Exception. Here, `list` is a function
		# which returns [], the default value.
		# https://docs.python.org/2/library/collections.html#collections.defaultdict

    def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size-3)
		seed_word, next_word = self.words[seed], self.words[seed+1]
		w1, w2 = seed_word, next_word
		gen_words = []
		for i in xrange(size):
			gen_words.append(w1)
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words)

shirley_file = open('shirley.txt')
import markovgen
# [brian] It's convention in python to put imports at the top of the file. It's sometimes
# useful to be able to quickly tell which modules a file uses.
markov = markovgen.Markov('shirley.txt')
markov.generate_markove_text()
