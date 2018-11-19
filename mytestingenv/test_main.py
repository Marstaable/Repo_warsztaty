import unittest
from main import add

#klasa jako scenariusz

class TestAddTestCase(unittest.TestCase):

    def test_if_two_positive_intigers_return_positive_intiger(self):
        # given
        a = 2
        b = 2
        #then
        expected = a + b
        result = add(a,b)
        self.assertEqual(result,expected)

    def test_if_positive_plus_zero_returns_positive(self):
        a = 2
        b = 0

        expected = 2
        result = add(a,b)
        self.assertEqual(expected,result)

