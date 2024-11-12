import unittest

from main import min_of_three_vars


class MinOfThreeVarsTestCase(unittest.TestCase):

    def test_min_a(self):
        res = min_of_three_vars(1, 2, 3)
        self.assertEqual(res, 1)
