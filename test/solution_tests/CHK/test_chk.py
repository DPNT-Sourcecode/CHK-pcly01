from lib.solutions.CHK import checkout_solution

class TestChk():
    def test_chk_with_name(self):
        assert checkout_solution.checkout('Wave') == 'Hello, Wave!'