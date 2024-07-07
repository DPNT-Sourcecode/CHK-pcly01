from lib.solutions.CHK import checkout_solution

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('A B C D') == 115

    def test_chk_three_a_offer(self):
        assert checkout_solution.checkout('A A A') == 130

    def test_chk_double_three_a_offer(self):
        assert checkout_solution.checkout('A A A A A A') == 260

    def test_chk_two_b_offer(self):
        assert checkout_solution.checkout('B B') == 45

    def test_chk_double_two_b_offer(self):
        assert checkout_solution.checkout('B B B B') == 90

    def test_chk_multiple_different_offers(self):
        assert checkout_solution.checkout('A A A B B') == 175

    def test_chk_complicated_list(self):
        assert checkout_solution.checkout('A A A B B C C C D D D') == 280

    def test_chk_lower_case_list(self):
        assert checkout_solution.checkout('a b c') == -1

    def test_chk_no_spaces(self):
        assert checkout_solution.checkout('ABC') == 100

    def test_chk_invalid_letter(self):
        assert checkout_solution.checkout('E') == -1

    def test_chk_no_input(self):
        assert checkout_solution.checkout('') == 0