import os

import pytest

import problems.euler as euler


@pytest.mark.euler
class TestEulerResults:

    """
    In each test, expected is a number confirmed to be the correct number via the project euler problem link included in each test.
    pytest.mark.parameterize was used in many cases to make the tests easily scalable, despite most failing with any other values being passed in.
    """

    @pytest.mark.parametrize("num_1, num_2, limit, expected", [(3, 5, 1000, 233168)])
    def test_problem_1(self, num_1, num_2, limit, expected):
        """
        https://projecteuler.net/problem=1

        Find the sum of all the multiples of 3 or 5 below 1000.
        """
        returned_value = euler.problem_1(num_1=num_1, num_2=num_2, limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("limit, expected", [(4000000, 4613732)])
    def test_problem_2(self, limit, expected):
        """
        https://projecteuler.net/problem=2

        By considering the terms in the Fibonacci sequence whose values do not exceed four million,
        find the sum of the even-valued terms.
        """
        returned_value = euler.problem_2(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("num, expected", [(600851475143, 6857)])
    def test_problem_3(self, num, expected):
        """
        https://projecteuler.net/problem=3

        What is the largest prime factor of the number 600851475143 ?
        """
        returned_value = euler.problem_3(num=num)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    def test_problem_4(self):
        """
        https://projecteuler.net/problem=4

        Find the largest palindrome made from the product of two 3-digit numbers.
        """
        expected = 906609
        returned_value = euler.problem_4()

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("n_min, n_max", [(1, 20)])
    def test_problem_5(self, n_min, n_max):
        """
        https://projecteuler.net/problem=5

        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
        """
        expected = 232792560
        returned_value = euler.problem_5(n_min=n_min, n_max=n_max)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [100])
    def test_problem_6(self, limit):
        """
        https://projecteuler.net/problem=6

        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
        """
        expected = 24174150
        returned_value = euler.problem_6(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("prime_count", [10001])
    def test_problem_7(self, prime_count):
        """
        https://projecteuler.net/problem=7

        What is the 10001st prime number?
        """
        expected = 104743
        returned_value = euler.problem_7(num=prime_count)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("adjacent", [13])
    def test_problem_8(self, adjacent):
        """
        https://projecteuler.net/problem=8

        Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
        What is the value of this product?
        """
        expected = 23514624000

        with open(os.path.join(os.getcwd(), "data", "problem_008.txt"), "r") as f:
            num = f.readlines()[0]

            returned_value = euler.problem_8(num=num, adjacent=adjacent)

            assert (
                expected == returned_value
            ), f"Expected {expected}, got {returned_value} instead."

    def test_problem_9(self):
        """
        https://projecteuler.net/problem=9

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
        """
        expected = 31875000
        returned_value = euler.problem_9(c=1000)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("below", [1999999])
    def test_problem_10(self, below):
        """
        https://projecteuler.net/problem=10

        Find the sum of all the primes below two million.
        """
        expected = 142913828922
        returned_value = euler.problem_10(num=below)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    def test_problem_11(self):
        """
        https://projecteuler.net/problem=11

        What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in a 20×20 grid?
        """
        expected = 70600674

        with open(os.path.join(os.getcwd(), "data", "problem_011.txt"), "r") as f:
            grid = [
                [int(i) for i in g.split(" ")]
                for g in [g.strip() for g in f.readlines()]
            ]

            returned_value = euler.problem_11(grid)

            assert (
                expected == returned_value
            ), f"Expected {expected}, got {returned_value} instead."

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
        expected = 76576500
        returned_value = euler.problem_12(expected_divs=divs)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("num_digits", [10])
    def test_problem_13(self, num_digits):
        """
        https://projecteuler.net/problem=13

        Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
        """
        expected = 5537376230

        with open(os.path.join(os.getcwd(), "data", "problem_013.txt"), "r") as f:
            numbers = [n for n in list(map(int, f))]

            returned_value = euler.problem_13(nums=numbers, num_digits=num_digits)

            assert (
                expected == returned_value
            ), f"Expected {expected}, got {returned_value} instead."

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
        expected = 837799
        returned_value = euler.problem_14(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("x, y", [(20, 20)])
    def test_problem_15(self, x, y):
        """
        https://projecteuler.net/problem=15

        Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

        How many such routes are there through a 20×20 grid?
        """
        expected = 137846528820
        returned_value = euler.problem_15(length=x, width=y)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("num, power", [(2, 1000)])
    def test_problem_16(self, num, power):
        """
        https://projecteuler.net/problem=16

        What is the sum of the digits of the number 2^1000?
        """
        expected = 1366
        returned_value = euler.problem_16(num=num, power=power)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

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
        expected = 21124
        returned_value = euler.problem_17()

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

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
        expected = 1074

        with open(os.path.join(os.getcwd(), "data", "problem_018.txt"), "r") as f:
            numbers = [
                [int(i) for i in num.split(" ") if num.split(" ")]
                for num in [line.strip() for line in f.readlines()]
            ]

            returned_value = euler.problem_18(numbers)

            assert (
                expected == returned_value
            ), f"Expected {expected}, got {returned_value} instead."

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
        expected = 171
        returned_value = euler.problem_19(start_year=start, end_year=end)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("number", [100])
    def test_problem_20(self, number):
        """
        https://projecteuler.net/problem=20

        n! means n × (n − 1) × ... × 3 × 2 × 1

        For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

        Find the sum of the digits in the number 100!
        """
        expected = 648
        returned_value = euler.problem_20(number=number)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [8000])
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
        expected = 31626
        returned_value = euler.problem_21(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

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
        expected = 871198282

        with open(os.path.join(os.getcwd(), "data", "problem_022.txt"), "r") as f:
            names = [name for name in list(map(str, f))]

            returned_value = euler.problem_22(names)

            assert (
                expected == returned_value
            ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [28123])
    def test_problem_23(self, limit):
        """
        https://projecteuler.net/problem=23

        A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example:
            The sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
            A number n is called deficient if the sum of its proper divisors is less than n,
                and it is called abundant if this sum exceeds n.
        As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
            as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
            than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any
            further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two
            abundant numbers is less than this limit.
        Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
        """
        expected = 4179871
        returned_value = euler.problem_23(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("value", ["0123456789"])
    def test_problem_24(self, value):
        """
        https://projecteuler.net/problem=24

        A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
        1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
        The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
        What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
        """
        expected = 2783915460
        returned_value = euler.problem_24(perm=1000000, chars=value)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("count", [1000])
    def test_problem_25(self, count):
        """
        https://projecteuler.net/problem=25

        What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
        """
        expected = 4782
        returned_value = euler.problem_25(count=count)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("limit", [999])
    def test_problem_26(self, limit):
        """
        https://projecteuler.net/problem=26

        Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
        """
        expected = 983
        returned_value = euler.problem_26(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

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
        pass

    @pytest.mark.parametrize("limit", [1001])
    def test_problem_28(self, limit):
        """
        https://projecteuler.net/problem=28

        Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

            21 22 23 24 25
            20  7  8  9 10
            19  6  1  2 11
            18  5  4  3 12
            17 16 15 14 13

        It can be verified that the sum of the numbers on the diagonals is 101.

        What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
        """
        expected = 669171001
        returned_value = euler.problem_28(limit=limit)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("num", [100])
    def test_problem_29(self, num):
        """
        https://projecteuler.net/problem=29

        Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

            2^2=4,  2^3=8,   2^4=16,  2^5=32
            3^2=9,  3^3=27,  3^4=81,  3^5=243
            4^2=16, 4^3=64,  4^4=256, 4^5=1024
            5^2=25, 5^3=125, 5^4=625, 5^5=3125

        If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:
            4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

        How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
        """
        expected = 9183
        returned_value = euler.problem_29(num=num)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("power", [5])
    def test_problem_30(self, power):
        """
        https://projecteuler.net/problem=30

        Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

            1634 = 1^4 + 6^4 + 3^4 + 4^4
            8208 = 8^4 + 2^4 + 0^4 + 8^4
            9474 = 9^4 + 4^4 + 7^4 + 4^4

            As 1 = 1^4 is not a sum it is not included.

        The sum of these numbers is 1634 + 8208 + 9474 = 19316.

        Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
        """
        expected = 443839
        returned_value = euler.problem_30(power=power)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    @pytest.mark.parametrize("coins, check", [([1, 2, 5, 10, 20, 50, 100, 200], 200)])
    def test_problem_31(self, coins, check):
        """
        https://projecteuler.net/problem=31

        In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

            1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

        It is possible to make £2 in the following way:

            1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

        How many ways can £2 be made using any number of coins?
        """
        expected = 73682
        returned_value = euler.problem_31(coins=coins, target=check)

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    def test_problem_32(self):
        """
        https://projecteuler.net/problem=32

        We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

        The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

        Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
        HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
        """
        expected = 45228
        returned_value = euler.problem_32()

        assert (
            expected == returned_value
        ), f"Expected {expected}, got {returned_value} instead."

    def test_problem_67(self):
        """
        https://projecteuler.net/problem=67

        Find the maximum total from top to bottom in get_problem_67_data() containing a triangle with one-hundred rows.
        NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether
        """
        expected = 7273

        with open(os.path.join(os.getcwd(), "data", "problem_067.txt"), "r") as f:
            numbers = [
                [int(i) for i in num.split(" ") if num.split(" ")]
                for num in [line.strip() for line in f.readlines()]
            ]

            returned_value = euler.problem_67(numbers)

            assert (
                expected == returned_value
            ), f"Expected {expected}, got {returned_value} instead."
