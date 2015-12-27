import unittest
from trie import Trie

class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add('CAT')
        self.trie.add('CAR')
        self.trie.add('CART')
        self.trie.add('DO')
        self.trie.add('DOG')
        self.trie.add('X')

    def test_root_children(self):
        root = self.trie.root

        self.assertEqual(3, len(root.children))
        self.assertTrue(root.children['C'])
        self.assertTrue(root.children['D'])
        self.assertTrue(root.children['X'])

    def test_single_letter(self):
        x_node = self.trie.root.children['X']
        self.assertEqual(0, len(x_node.children))
        self.assertTrue(x_node.is_word)

    def test_prefix_is_also_word(self):
        d_node = self.trie.root.children['D']
        self.assertFalse(d_node.is_word)

        do_node = d_node.children['O']
        self.assertTrue(do_node.is_word)

        dog_node = do_node.children['G']
        self.assertTrue(dog_node.is_word)

    def test_multiple_branches_are_words(self):
        ca_node = self.trie.root.children['C'].children['A']
        self.assertFalse(ca_node.is_word)

        cat_node = ca_node.children['T']
        self.assertTrue(cat_node.is_word)

        car_node = ca_node.children['R']
        self.assertTrue(car_node.is_word)

        cart_node = car_node.children['T']
        self.assertTrue(cart_node.is_word)

if __name__ == '__main__':
    unittest.main()        