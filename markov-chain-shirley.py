import random

class Node(object):
    def __init__(self):
        self.frequency = 1
        self.edges = dict()
        self.p_ranges = []

# frequencies into nodes. value is the node which tracks the frequency that that word occurred
def parse_file(input_file):
    starting_words = set()
    ending_words = set()
    graph = dict()
    previous = None
    in_sentence = False
    for line in input_file:
        words = line.strip().split(" ")
        for word in words:
            if len(word) == 0:
                continue
            if not in_sentence:
                starting_words.add(word)
                in_sentence = True
            elif word[-1] == '.':
                ending_words.add(word)
                in_sentence = False
            if word in graph:
                node = graph[word]
                node.frequency += 1
            else:
                graph[word] = Node()
            if previous:
                node = graph[previous]
                if word in node.edges:
                    node.edges[word] += 1
                else:
                    node.edges[word] = 1
            previous = word
    return (graph, starting_words, ending_words)

def preprocess_graph(graph):
    for key,node in graph.items():
        probabilities = dict()
        for key,value in node.edges.items():
            probabilities[key] = value/float(node.frequency)
        s = 0
        p_ranges = []
        for key,value in probabilities.items():
            s += value
            p_ranges.append((s,key))
        node.p_ranges = p_ranges

def next_word(node):
    r = random.uniform(0,1)
    for t in node.p_ranges:
        if r < t[0]:
            return t[1]
    return None

def generate_sentence(graph, starting_words, ending_words):
    prev = random.choice(list(starting_words))
    string = prev
    while True:
        p = graph[prev]
        n_word = next_word(p)
        if n_word is None:
            break
        string += " "
        string += n_word
        if n_word in ending_words:
            break
        prev = n_word
    return string

input_file = open('shirley.txt', 'r')
graph, starting_words, ending_words = parse_file(input_file)
preprocess_graph(graph)
string = ""
while len(string) < 25 or len(string) > 150:
    string = generate_sentence(graph, starting_words, ending_words)
print(string)
