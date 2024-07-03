from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        
    def test_sum_upperbounds(self):
        assert sum_solution.compute(100, 100) == 200
    
    def test_sum_above_limit(self):
        assert sum_solution.compute(101, 100) == 

