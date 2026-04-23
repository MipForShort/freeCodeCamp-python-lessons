class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str):
        return sum(ord(c) for c in key)

    def add(self, key: str, value):
        index = self.hash(key)

        if index not in self.collection:
            self.collection[index] = {key: value}
        else:
            self.collection[index][key] = value

    def remove(self, key: str):
        index = self.hash(key)

        if index in self.collection and key in self.collection[index]:
            del self.collection[index][key]

    def lookup(self, key: str):
        index = self.hash(key)

        if index in self.collection and key in self.collection[index]:
            return self.collection[index][key]
        
        return None
