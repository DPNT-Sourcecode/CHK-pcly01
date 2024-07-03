from lib.solutions.HLO import sum_solution
import pytest

class TestHlo():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3