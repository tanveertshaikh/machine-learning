import unittest
from hw1 import prime_nums_reversed
from hw1 import string_explosion
from hw1 import consecutive

class TestQ01A(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_nums_one(self):
        """Evaluate prime_nums_reversed(1)"""
        self.assertEqual(prime_nums_reversed(1), '')
        self.assertEqual(prime_nums_reversed(5), '5 3 2')
    
    def test_nums_other(self):
        self.assertEqual(prime_nums_reversed(5), '5 3 2')
        self.assertEqual(prime_nums_reversed(10), '7 5 3 2')
        self.assertEqual(prime_nums_reversed(50), '47 43 41 37 31 29 23 19 17 13 11 7 5 3 2')
        self.assertEqual(prime_nums_reversed(100), '97 89 83 79 73 71 67 61 59 53 47 43 41 37 31 29 23 19 17 13 11 7 5 3 2')

    def test_string_explosion(self):
        self.assertEqual(string_explosion(''), '')
        self.assertEqual(string_explosion('   '), '      ')
        self.assertEqual(string_explosion(None), '')
        self.assertEqual(string_explosion('Code'), 'Codeodedee')
        self.assertEqual(string_explosion('data!'), 'data!ata!ta!a!!')
        self.assertEqual(string_explosion('hi'), 'hii')
        self.assertEqual(string_explosion('h'), 'h')
        
    def test_consecutive(self):
        """Evaluate prime_nums_reversed(1)"""
        self.assertEqual(consecutive([50, 34, 3, 15]), False)
        self.assertEqual(consecutive([7, 3, 20, 21, 8]), True)
        self.assertEqual(consecutive([-41,40]), False)
        self.assertEqual(consecutive([-1,0]), True)
        self.assertEqual(consecutive([-41,-40]), True)
        self.assertEqual(consecutive([]), False)
        self.assertEquals(consecutive([-1, 0, 3, 4]), True)
        self.assertEquals(consecutive([-1, 2, -4]), False)
        