from lib.solutions.CHK import checkout_solution

class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('A B C D E F') == 165

    def test_chk_two_e(self):
        assert checkout_solution.checkout('E E') == 80

    def test_chk_two_e_and_b_offer(self):
        assert checkout_solution.checkout('E E B') == 80

    def test_chk_two_f(self):
        assert checkout_solution.checkout('F F') == 20

    def test_chk_three_f(self):
        assert checkout_solution.checkout('F F F') == 20

    def test_chk_three_a_offer(self):
        assert checkout_solution.checkout('A A A') == 130

    def test_chk_double_three_a_offer(self):
        assert checkout_solution.checkout('A A A A A A') == 250

    def test_chk_five_a_offer(self):
        assert checkout_solution.checkout('A A A A A') == 200

    def test_chk_five_a_and_three_a_offer(self):
        assert checkout_solution.checkout('A A A A A A A A') == 330

    def test_chk_two_b_offer(self):
        assert checkout_solution.checkout('B B') == 45

    def test_chk_double_two_b_offer(self):
        assert checkout_solution.checkout('B B B B') == 90

    def test_chk_three_s_offer(self):
        assert checkout_solution.checkout('S S S') == 45

    def test_chk_three_for_fourtyfive_offer(self):
        assert checkout_solution.checkout('T X Y') == 45

    def test_chk_double_three_for_fourtyfive_offer(self):
        assert checkout_solution.checkout('T X Y S Z T') == 90

    def test_chk_multiple_different_offers(self):
        assert checkout_solution.checkout('A A A B B') == 175

    def test_chk_multi_offer_remove_order(self):
        assert checkout_solution.checkout('Z X Z Z') == 62

    def test_chk_complicated_list(self):
        assert checkout_solution.checkout('A A A B B C C C D D D') == 280

    def test_chk_lower_case_list(self):
        assert checkout_solution.checkout('a b c') == -1

    def test_chk_no_spaces(self):
        assert checkout_solution.checkout('ABC') == 100

    def test_chk_invalid_letter(self):
        assert checkout_solution.checkout('!') == -1

    def test_chk_no_input(self):
        assert checkout_solution.checkout('') == 0