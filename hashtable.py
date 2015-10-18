# coded by Isabella Cai

class HashTable(object):
    def __init__(self, capacity):
        super(HashTable, self).__init__()
        self.size = 0
        self.capacity = capacity # number of bins
        self.hash = self.capacity * [None]

    def set(self, key, value):
        insertion_index = self.find(key)
        if insertion_index == -1:
            return False
        if self.hash[insertion_index] is None:
            self.size += 1
        self.hash[insertion_index] = (key,value)
        return True

    def get(self, key):
        insertion_index = self.find(key)
        if insertion_index == -1:
            return None
        t = self.hash[insertion_index]
        if not t:
            return None
        return t[1]

    def delete(self, key):
        insertion_index = self.find(key)
        if insertion_index == -1:
            return None
        t = self.hash[insertion_index]
        if not t:
            return None
        self.size -= 1
        self.hash[insertion_index] = None
        return t[1]

    def find(self, key):
        insertion_index = hash(key) % self.capacity
        while insertion_index < self.capacity - 1:
            if self.hash[insertion_index] is None or key == self.hash[insertion_index][0]:
                return insertion_index
            insertion_index += 1
        insertion_index = 0
        while insertion_index < hash(key) % self.capacity:
            if self.hash[insertion_index] is None or key == self.hash[insertion_index][0]:
                return insertion_index
            insertion_index += 1
        return -1

    def load(self):
        return self.size / float(self.capacity)

h = HashTable(6)
h.set("Logan",10)
print(h.hash)
h.set("Isabella",9)
print(h.hash)
h.set("Isabella",8)
print(h.hash)
print("Strawberries", h.get("Strawberries"))
print("Isabella", h.get("Isabella"))
print("Load", h.load())
print("Delete", h.delete("Isabella"))
print(h.hash)
print("Delete", h.delete("Isabella2"))
print(h.hash)
