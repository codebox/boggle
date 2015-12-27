import unittest
from board_search import board_search
from board import Board
from trie import Trie

class BoardSearchTest(unittest.TestCase):
    def setUp(self):
        self.board = Board([['C', 'A', 'R'], ['D', 'O', 'T'], ['X', 'G', 'X']])
        self.trie = Trie()

    def test_search_with_no_words(self):
        self.assertEquals(set(), board_search(self.board, self.trie))

    def test_search_with_words(self):
        self.trie.add('CAT')
        self.trie.add('CAR')
        self.trie.add('CART')
        self.trie.add('DO')
        self.trie.add('DOG')
        self.trie.add('ABSENT')
        self.trie.add('DOGS')

        results = board_search(self.board, self.trie)

        self.assertEquals(set(['CAT', 'CAR', 'CART', 'DO', 'DOG']), results)

    def test_letter_q(self):
        self.board = Board([['Q', 'I'], ['T', 'X']])
        self.trie.add('QUIT')

        self.assertEquals(set(['QUIT']), board_search(self.board, self.trie))

if __name__ == '__main__':
    unittest.main()        