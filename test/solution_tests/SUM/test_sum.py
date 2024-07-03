from lib.solutions.SUM import sum_solution
import unittest


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_upperbounds(self):
        assert sum_solution.compute(100, 100) == 200

    def test_sum_lowerbounds(self):
        assert sum_solution.compute(0, 0) == 0

    def test_sum_above_limit(self):
        self.assertRaises(ValueError, sum_solution.compute(101, 100))

    def test_sum_negative_integer(self):
        self.assertRaises(ValueError, sum_solution.compute(-1, 100))






