import unittest
import numpy as np
from hw1 import bowl_cost
from hw1 import amount_spent
from hw1 import new_price

class TestQ02A(unittest.TestCase):
    def setUp(self):
        pass

    def test_one_three_five(self):
        """Evaluate bowl_cost([1, 3, 5])"""
        self.assertTrue(np.array_equal(bowl_cost([1, 3, 5]), np.array([27, 42, 30, 50])))
        
    def test_def_amount_spent(self):
        v = np.array([1,3,5])
        B = np.array([
        [3,3,3],
        [2,0,8],
        [0,5,3],
        [0,0,10]
        ])
        self.assertTrue(np.array_equal(amount_spent(v,B), np.array([84, 149, 500])))
