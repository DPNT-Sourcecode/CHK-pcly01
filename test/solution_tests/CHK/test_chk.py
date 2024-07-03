from lib.solutions.CHK import checkout_solution
import pytest

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('A B C D') == 115

    def test_chk_three_a_offer(self):
        assert checkout_solution.checkout('A A A') == 130

    def test_chk_two_b_offer(self):
        assert checkout_solution.checkout('B B') == 45

    def test_chk_invalid_letter(self):
            with pytest.raises(ValueError):
                checkout_solution.checkout('E')