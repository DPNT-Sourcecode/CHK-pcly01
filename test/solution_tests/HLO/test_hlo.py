from lib.solutions.HLO import hello_solution
import pytest

class TestHlo():
    def test_hlo_with_name(self):
        assert hello_solution.hello('Wave') == 'Hello, Wave!'
       
    def test_hlo_test_capitalization(self):
        assert hello_solution.hello('wave') == 'Hello, Wave!'
        
    def test_hlo_test_capitalization(self):
        assert hello_solution.hello('wave') == 'Hello, Wave!'