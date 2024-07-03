from lib.solutions.HLO import hello_solution
import pytest

class TestHlo():
    def test_hlo_with_name(self):
        assert hello_solution.hello('Wave') == 'Hello, Wave!'

    def test_hlo_test_no_name_provided(self):
        with pytest.raises(ValueError):
            hello_solution.hello('')