import os

import pytest

import problems.euler as euler


@pytest.mark.euler
class TestEulerResults:

    """
    In each test, expected_value is a number confirmed to be the correct number via the project euler problem link included in each test.
    pytest.mark.parameterize was used in many cases to make the tests easily scalable, despite in these cases any other values will likely result in failure.
    """

    @pytest.mark.parametrize("num_1, num_2, limit", [(3, 5, 1000)])
    def test_problem_1(self, num_1, num_2, limit):
        """
        https://projecteuler.net/problem=1

        Find the sum of all the multiples of 3 or 5 below 1000.
        """
        expected_value = 233168
        returned_value = euler.problem_1(num_1=num_1, num_2=num_2, limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [4000000])
    def test_problem_2(self, limit):
        """
        https://projecteuler.net/problem=2

        By considering the terms in the Fibonacci sequence whose values do not exceed four million,
        find the sum of the even-valued terms.
        """
        expected_value = 4613732
        returned_value = euler.problem_2(limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("num", [600851475143])
    def test_problem_3(self, num):
        """
        https://projecteuler.net/problem=3

        What is the largest prime factor of the number 600851475143 ?
        """
        expected_value = 6857
        returned_value = euler.problem_3(num=num)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_4(self):
        """
        https://projecteuler.net/problem=4

        Find the largest palindrome made from the product of two 3-digit numbers.
        """
        expected_value = 906609
        returned_value = euler.problem_4()

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("n_min, n_max", [(1, 20)])
    def test_problem_5(self, n_min, n_max):
        """
        https://projecteuler.net/problem=5

        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
        """
        expected_value = 232792560
        returned_value = euler.problem_5(n_min=n_min, n_max=n_max)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [100])
    def test_problem_6(self, limit):
        """
        https://projecteuler.net/problem=6

        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
        """
        expected_value = 24174150
        returned_value = euler.problem_6(limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("prime_count", [10001])
    def test_problem_7(self, prime_count):
        """
        https://projecteuler.net/problem=7

        What is the 10001st prime number?
        """
        expected_value = 104743
        returned_value = euler.problem_7(num=prime_count)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("adjacent", [13])
    def test_problem_8(self, adjacent):
        """
        https://projecteuler.net/problem=8

        Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
        What is the value of this product?
        """
        expected_value = 23514624000

        with open(os.path.join(os.getcwd(), "data", "problem_008.txt"), "r") as f:
            num = f.readlines()[0]

            returned_value = euler.problem_8(num=num, adjacent=adjacent)

            assert (
                expected_value == returned_value
            ), f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_9(self):
        """
        https://projecteuler.net/problem=9

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
        """
        expected_value = 31875000
        returned_value = euler.problem_9(c=1000)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("below", [1999999])
    def test_problem_10(self, below):
        """
        https://projecteuler.net/problem=10

        Find the sum of all the primes below two million.
        """
        expected_value = 142913828922
        returned_value = euler.problem_10(num=below)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_11(self):
        """
        https://projecteuler.net/problem=11

        What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in a 20×20 grid?
        """
        expected_value = 70600674

        with open(os.path.join(os.getcwd(), "data", "problem_011.txt"), "r") as f:
            grid = [
                [int(i) for i in g.split(" ")]
                for g in [g.strip() for g in f.readlines()]
            ]

            returned_value = euler.problem_11(grid)

            assert (
                expected_value == returned_value
            ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.slow
    @pytest.mark.parametrize("divs", [500])
    def test_problem_12(self, divs):
        """
        https://projecteuler.net/problem=12

        The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

        Let us list the factors of the first seven triangle numbers:

             1: 1
             3: 1,3
             6: 1,2,3,6
            10: 1,2,5,10
            15: 1,3,5,15
            21: 1,3,7,21
            28: 1,2,4,7,14,28

        We can see that 28 is the first triangle number to have over five divisors.

        What is the value of the first triangle number to have over five hundred divisors?
        """
        expected_value = 76576500
        returned_value = euler.problem_12(expected_divs=divs)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("num_digits", [10])
    def test_problem_13(self, num_digits):
        """
        https://projecteuler.net/problem=13

        Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
        """
        expected_value = 5537376230

        with open(os.path.join(os.getcwd(), "data", "problem_013.txt"), "r") as f:
            numbers = [n for n in list(map(int, f))]

            returned_value = euler.problem_13(nums=numbers, num_digits=num_digits)

            assert (
                expected_value == returned_value
            ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.slow
    @pytest.mark.parametrize("limit", [999999])
    def test_problem_14(self, limit):
        """
        https://projecteuler.net/problem=14

        The following iterative sequence is defined for the set of positive integers:
            n → n/2 (n is even)
            n → 3n + 1 (n is odd)

        Using the rule above and starting with 13, we generate the following sequence:
            13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
        Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?
        """
        expected_value = 837799
        returned_value = euler.problem_14(limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("x, y", [(20, 20)])
    def test_problem_15(self, x, y):
        """
        https://projecteuler.net/problem=15

        Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

        How many such routes are there through a 20×20 grid?
        """
        expected_value = 137846528820
        returned_value = euler.problem_15(length=x, width=y)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("num, power", [(2, 1000)])
    def test_problem_16(self, num, power):
        """
        https://projecteuler.net/problem=16

        What is the sum of the digits of the number 2^1000?
        """
        expected_value = 1366
        returned_value = euler.problem_16(num, power)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_17(self):
        """
        https://projecteuler.net/problem=17

        If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
            how many letters would be used?
        NOTE:
            Do not count spaces or hyphens.
            For example, 342 (three hundred and forty-two) contains 23 letters and
                115 (one hundred and fifteen) contains 20 letters.
            The use of "and" when writing out numbers is in compliance with British usage.
        """
        expected_value = 21124
        returned_value = euler.problem_17()

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_18(self):
        """
        https://projecteuler.net/problem=18

        By starting at the top of the triangle below and moving to adjacent numbers on the row below,
            the maximum total from top to bottom is 23.

                       3
                      7 4
                     2 4 6
                    8 5 9 3

        That is, 3 + 7 + 4 + 9 = 23.

        Find the maximum total from top to bottom of the triangle provided
        """
        expected_value = 1074

        with open(os.path.join(os.getcwd(), "data", "problem_018.txt"), "r") as f:
            numbers = [
                [int(i) for i in num.split(" ") if num.split(" ")]
                for num in [line.strip() for line in f.readlines()]
            ]

            returned_value = euler.problem_18(numbers)

            assert (
                expected_value == returned_value
            ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("start, end", [(1901, 2001)])
    def test_problem_19(self, start, end):
        """
        https://projecteuler.net/problem=19

        You are given the following information, but you may prefer to do some research for yourself.

            * 1 Jan 1900 was a Monday.
            * Thirty days has September,
                April, June and November.
                All the rest have thirty-one,
                Saving February alone,
                Which has twenty-eight, rain or shine.
                And on leap years, twenty-nine.
            * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

        How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
        """
        expected_value = 171
        returned_value = euler.problem_19(start_year=start, end_year=end)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("number", [100])
    def test_problem_20(self, number):
        """
        https://projecteuler.net/problem=20

        n! means n × (n − 1) × ... × 3 × 2 × 1

        For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

        Find the sum of the digits in the number 100!
        """
        expected_value = 648
        returned_value = euler.problem_20(number=number)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.slow
    @pytest.mark.parametrize("limit", [10000])
    def test_problem_21(self, limit):
        """
        https://projecteuler.net/problem=21

        Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
        If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
            amicable numbers.

        For example:
            The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
            The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

        Evaluate the sum of all the amicable numbers under 10000.
        """
        expected_value = 31626
        returned_value = euler.problem_21(limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    def test_problem_22(self):
        """
        https://projecteuler.net/problem=22

        Using data.get_problem_22_data(), begin by sorting it into alphabetical order.
            Then working out the alphabetical value for each name,
            multiply this value by its alphabetical position in the list to obtain a name score.

        For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
            is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

        What is the total of all the name scores in the file?
        """
        expected_value = 871198282

        with open(os.path.join(os.getcwd(), "data", "problem_022.txt"), "r") as f:
            names = [name for name in list(map(str, f))]

            returned_value = euler.problem_22(names)

            assert (
                expected_value == returned_value
            ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [28123])
    def test_problem_23(self, limit):
        """
        https://projecteuler.net/problem=23

        A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example:
            The sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
            A number n is called deficient if the sum of its proper divisors is less than n
                and it is called abundant if this sum exceeds n.
        As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
            as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
            than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any
            further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two
            abundant numbers is less than this limit.
        Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
        """
        expected_value = 4179871
        returned_value = euler.problem_23(limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("value", ["0123456789"])
    def test_problem_24(self, value):
        """
        https://projecteuler.net/problem=24

        A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
        1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
        The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
        What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
        """
        expected_value = 2783915460
        returned_value = euler.problem_24(perm=1000000, chars=value)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("count", [1000])
    def test_problem_25(self, count):
        """
        https://projecteuler.net/problem=25

        What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
        """
        expected_value = 4782
        returned_value = euler.problem_25(count=count)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [999])
    def test_problem_26(self, limit):
        """
        https://projecteuler.net/problem=26

        Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
        """
        expected_value = 983
        returned_value = euler.problem_26(limit=limit)

        assert (
            expected_value == returned_value
        ), f"Expected {expected_value}, got {returned_value} instead."

    @pytest.mark.skip(reason="Have not solved yet")
    def test_problem_27(self):
        """
        https://projecteuler.net/problem=27

        Considering quadratics of the form:

            n2+an+b, where |a|<1000 and |b|≤1000

            where |n| is the modulus/absolute value of n
                e.g. |11|=11 and |−4|=4

        Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
            primes for consecutive values of n, starting with n=0.
        """

    def test_problem_67(self):
        """
        https://projecteuler.net/problem=67

        Find the maximum total from top to bottom in get_problem_67_data() containing a triangle with one-hundred rows.
        NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether
        """
        expected_value = 7273

        with open(os.path.join(os.getcwd(), "data", "problem_067.txt"), "r") as f:
            numbers = [
                [int(i) for i in num.split(" ") if num.split(" ")]
                for num in [line.strip() for line in f.readlines()]
            ]

            returned_value = euler.problem_67(numbers)

            assert (
                expected_value == returned_value
            ), f"Expected {expected_value}, got {returned_value} instead."
