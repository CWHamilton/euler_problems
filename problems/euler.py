from functools import reduce

import data.get_data as ed
import problems.euler_functions as ef


def problem_1(total: int = 1000) -> int:
    """
    https://projecteuler.net/problem=1
    Find the sum of all the multiples of 3 or 5 below 1000.
    :param total:
    :return:
    """
    r = 0

    for i in range(total):
        if i % 3 == 0 or i % 5 == 0:
            r += i
    return r


def problem_2(exceed: int = 4000000) -> int:
    """
    https://projecteuler.net/problem=2
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
        find the sum of the even-valued terms.
    :param exceed:
    :return:
    """
    a = 1
    b = 1
    r = 0

    while b <= exceed:
        c = b
        b = b + a
        a = c

        if b % 2 == 0:
            r += b

    return r


def problem_3(num: int = 600851475143) -> int:
    """
    https://projecteuler.net/problem=3
    What is the largest prime factor of the number 600851475143 ?
    :return:
    """
    i = 2

    while i * i < num:
        while num % i == 0:
            num /= i
        i += 1

    return int(num)


def problem_4() -> int:
    """
    https://projecteuler.net/problem=4
    Find the largest palindrome made from the product of two 3-digit numbers.
    :return:
    """
    p = []
    for i in range(100, 999):
        for n in range(100, 999):
            num = str(i * n).split()[0]
            if len(num) == 6:
                if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
                    p.append(i * n)

    return max(p)


def problem_5(num: int = 20) -> int:
    """
    https://projecteuler.net/problem=5
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    :return:
    """
    return ef.smallest_multiple(num)


def problem_6(num: int = 100) -> int:
    """
    https://projecteuler.net/problem=6
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    :return:
    """
    sum_squares = ef.sum_squares(num)
    square_sums = ef.square_sum(num)
    return square_sums - sum_squares


def problem_7(num: int = 10001) -> int:
    """
    https://projecteuler.net/problem=7
    What is the 10001st prime number?
    :return:
    """
    return ef.find_prime(num)


def problem_8(adjacent: int = 13) -> int:
    """
    https://projecteuler.net/problem=8
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
        What is the value of this product?
    :param: adjacent
    :return:
    """
    num = str(ed.get_problem_8_data())
    max_v = 0

    for i, n, in enumerate(num):
        value = reduce((lambda x, y: x * y), map(int, (num[i:i + adjacent])))

        if value > max_v:
            max_v = value

    return max_v


def problem_9(c: int = 1000) -> int:
    """
    https://projecteuler.net/problem=9
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
    :return:
    """
    for num in range(1, c):
        for a in range(num, c - num):
            b = c - num - a
            if num * num + a * a == b * b:
                return num * a * b


def problem_10(num: int = 1999999) -> int:
    """
    https://projecteuler.net/problem=10
    Find the sum of all the primes below two million.
    :param num:
    :return:
    """
    return ef.sum_primes(num)


def problem_11(numbers: list = ed.get_problem_11_data()) -> int:
    """
    https://projecteuler.net/problem=11
    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
        in a 20×20 grid?
    :param numbers:
    :return:
    """
    return ef.get_greatest_product_in_grid(numbers)


def problem_12(expected_divs: int = 500) -> int:
    """
    https://projecteuler.net/problem=12
    What is the value of the first triangle number to have over five hundred divisors?
    :return:
    """
    n = 28
    while True:
        triangle_number = n * (n + 1) / 2
        n = n + 1
        dic = {}
        i = 2

        while i <= triangle_number:
            if triangle_number % i == 0:
                triangle_number = triangle_number / i

                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
                i -= 1
            i += 1

        powers = map(lambda x: (x + 1), dic.values())

        divisors = reduce(lambda x, y: x * y, powers)

        if divisors > expected_divs:
            break
    return int((n - 1) * n / 2)


def problem_13(nums: list = ed.get_problem_13_data()) -> int:
    """
    https://projecteuler.net/problem=13
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    :param nums:
    :return:
    """
    num_sum = 0
    for i in nums:
        num_sum += i

    return int(str(num_sum)[0:10])


def problem_14(limit: int = 1000000):
    """
    The following iterative sequence is defined for the set of positive integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    :param: limit
    :return:
    """
    dic = {n: 0 for n in range(1, limit)}
    dic[1] = 1
    dic[2] = 2

    for n in range(3, limit, 1):
        counter = 0
        o_num = n

        while n > 1:
            if n < o_num:
                dic[o_num] = dic[n] + counter
                break
            if n % 2 == 0:
                n = n / 2
                counter += 1
            else:
                n = (3 * n) + 1
                counter += 1

    return list(dic.values()).index(max(dic.values())) + 1


def problem_15(l: int = 20, w: int = 20) -> int:
    """
    https://projecteuler.net/problem=15
    How many such routes are there through a 20×20 grid?
    :return:
    """
    return ef.get_path_results(l, w)


def problem_16(num: int = 1000) -> int:
    """
    https://projecteuler.net/problem=16
    What is the sum of the digits of the number 2^1000?
    """
    r = 0
    for i in str(2 ** num):
        r += int(i)

    return r


def problem_17() -> int:
    dic = {n: 0 for n in range(0, 1001)}
    dic[0] = 0  # ''
    dic[1] = len('one')
    dic[2] = len('two')
    dic[3] = len('three')
    dic[4] = len('four')
    dic[5] = len('five')
    dic[6] = len('six')
    dic[7] = len('seven')
    dic[8] = len('eight')
    dic[9] = len('nine')
    dic[10] = len('ten')
    dic[11] = len('eleven')
    dic[12] = len('twelve')
    dic[13] = len('thirteen')
    dic[14] = len('fourteen')
    dic[15] = len('fifteen')
    dic[16] = len('sixteen')
    dic[17] = len('seventeen')
    dic[18] = len('eighteen')
    dic[19] = len('nineteen')
    dic[20] = len('twenty')
    dic[30] = len('thirty')
    dic[40] = len('forty')
    dic[50] = len('fifty')
    dic[60] = len('sixty')
    dic[70] = len('seventy')
    dic[80] = len('eighty')
    dic[90] = len('ninety')

    for i in range(21, 100):
        tens = int(i / 10) * 10
        ones = i - tens
        dic[i] = dic[tens] + dic[ones]

    for i in range(100, 1000):
        hundreds = int(i / 100)
        tens_ones = i - hundreds * 100

        if tens_ones == 0:
            dic[i] = dic[hundreds] + len('hundred')
        else:
            dic[i] = dic[hundreds] + len('hundredand') + dic[tens_ones]

    dic[1000] = len('onethousand')

    return sum(dic.values())