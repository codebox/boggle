class Trie:
    def __init__(self):
        self.root = Node('')

    def add(self, word):
        parent = self.root
        while word:
            first_letter = word[0]
            remainder = word[1:]

            child = parent.get_child(first_letter)
            if not child:
                child = parent.add_child(first_letter)

            if not remainder:
                child.is_word = True

            parent = child
            word = remainder

class Node:
    def __init__(self, value):
        self.value = value
        self.is_word = False
        self.children = {}

    def get_child(self, letter):
        if self.children.has_key(letter):
            return self.children.get(letter)

    def add_child(self, letter):
        child = Node(self.value + letter)
        self.children[letter] = child
        return child