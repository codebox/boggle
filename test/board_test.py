import unittest
from boggle import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])

    def test_get_letter(self):                
        self.assertEquals('A', self.board.get_letter(0,0))
        self.assertEquals('B', self.board.get_letter(1,0))
        self.assertEquals('I', self.board.get_letter(2,2))
        
    def test_neighbours_corner(self): 
        self.assertEquals(set(self.board.get_neighbours(0,0)), set([(1,0), (1,1), (0,1)]))
        self.assertEquals(set(self.board.get_neighbours(2,0)), set([(1,0), (1,1), (2,1)]))
        self.assertEquals(set(self.board.get_neighbours(2,2)), set([(2,1), (1,1), (1,2)]))
        self.assertEquals(set(self.board.get_neighbours(0,2)), set([(0,1), (1,1), (1,2)]))

    def test_neighbours_edge(self): 
        self.assertEquals(set(self.board.get_neighbours(1,0)), set([(0,0), (0,1), (1,1), (2,1), (2,0)]))
        self.assertEquals(set(self.board.get_neighbours(2,1)), set([(1,0), (2,0), (1,1), (1,2), (2,2)]))
        self.assertEquals(set(self.board.get_neighbours(1,2)), set([(0,1), (1,1), (2,1), (0,2), (2,2)]))
        self.assertEquals(set(self.board.get_neighbours(0,1)), set([(0,0), (1,0), (1,1), (1,2), (0,2)]))

    def test_neighbours_center(self): 
        self.assertEquals(set(self.board.get_neighbours(1,1)), set([(0,0), (1,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2)]))

if __name__ == '__main__':
    unittest.main()        