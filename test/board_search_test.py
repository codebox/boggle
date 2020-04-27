import unittest
from board_search import board_search
from board import Board
from trie import Trie

class BoardSearchTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_search_with_no_words(self):
        board = Board([['C', 'A', 'R'], ['D', 'O', 'T'], ['X', 'G', 'X']])
        self.assertEquals(set(), board_search(board, self.trie))

    def test_search_with_words(self):
        board = Board([['C', 'A', 'R'], ['D', 'O', 'T'], ['X', 'G', 'X']])
        self.trie.add('CAT')
        self.trie.add('CAR')
        self.trie.add('CART')
        self.trie.add('DO')
        self.trie.add('DOG')
        self.trie.add('ABSENT')
        self.trie.add('DOGS')

        results = board_search(board, self.trie)

        self.assertEquals(set(['CAT', 'CAR', 'CART', 'DO', 'DOG']), results)

    def test_letter_q(self):
        board = Board([['Q', 'I'], ['T', 'X']])
        self.trie.add('QUIT')
        self.trie.add('QIT')

        self.assertEquals(set(['QUIT']), board_search(board, self.trie))

    def test_letter_q_bug(self):
        board = Board([['Q', 'A'], ['B', 'O']])
        self.trie.add('BQ')
        self.trie.add('BA')

        self.assertEquals(set(['BA']), board_search(board, self.trie))


if __name__ == '__main__':
    unittest.main()        