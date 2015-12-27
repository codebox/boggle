import unittest
from answers import Answers

class AnswersTest(unittest.TestCase):
    def setUp(self):
        self.answers = Answers()

    def test_empty(self):
        self.assertEquals(0, self.answers._calc_points())

    def test_duplicates(self):
        word = 'abc'

        self.answers.add([word, word, word])
        self.assertEquals(1, self.answers._calc_points())

        self.answers.add([word])
        self.assertEquals(1, self.answers._calc_points())

    def test_dict(self):
        self.answers.add(['aaa', 'bbb', 'cccc'])

        d = self.answers._make_dict()

        self.assertEquals(['aaa', 'bbb'], d[3])
        self.assertEquals(['cccc'], d[4])

if __name__ == '__main__':
    unittest.main()        