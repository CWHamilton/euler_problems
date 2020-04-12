import pytest

import problems.euler as euler


@pytest.mark.euler
class TestEulerResults:

    def test_problem_1(self):
        expected_value = 233168
        returned_value = euler.problem_1()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_2(self):
        expected_value = 4613732
        returned_value = euler.problem_2()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_3(self):
        expected_value = 6857
        returned_value = euler.problem_3()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_4(self):
        expected_value = 906609
        returned_value = euler.problem_4()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_5(self):
        expected_value = 232792560
        returned_value = euler.problem_5()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_6(self):
        expected_value = 24174150
        returned_value = euler.problem_6()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_7(self):
        expected_value = 104743
        returned_value = euler.problem_7()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_8(self):
        expected_value = 23514624000
        returned_value = euler.problem_8()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_9(self):
        expected_value = 31875000
        returned_value = euler.problem_9()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_10(self):
        expected_value = 142913828922
        returned_value = euler.problem_10()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_11(self):
        expected_value = 70600674
        returned_value = euler.problem_11()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.slow
    def test_problem_12(self):
        expected_value = 76576500
        returned_value = euler.problem_12()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_13(self):
        expected_value = 5537376230
        returned_value = euler.problem_13()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_14(self):
        expected_value = 837799
        returned_value = euler.problem_14()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_15(self):
        expected_value = 137846528820
        returned_value = euler.problem_15()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_16(self):
        expected_value = 1366
        returned_value = euler.problem_16()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_17(self):
        expected_value = 21124
        returned_value = euler.problem_17()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_18(self):
        expected_value = 1074
        returned_value = euler.problem_18()

        assert expected_value == returned_value, f"Expected {expected_value}, got {returned_value} instead."
