import re
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


def problem_18() -> int:
    """
    https://projecteuler.net/problem=18
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
        the maximum total from top to bottom is 23.

                   3
                  7 4
                 2 4 6
                8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    number = \
        '''\
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

    number = number.strip().split('\n')

    for i in range(1, len(number)):
        number[i] = number[i].strip().split(' ')
        number[i] = [int(x) for x in number[i]]

    number[0] = [75]
    return int(ef.find_max_sum_path(number))


def problem_19() -> int:
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
    return int(str(ef.get_num_dates(1901, 2001)))


def problem_20() -> int:
    """
    https://projecteuler.net/problem=20
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """
    factorial = str(ef.factorial(100))
    r = 0
    for i in factorial:
        r += int(i)

    return r


def problem_21(limit: int = 10000) -> int:
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
    return int(sum(ef.find_amicable(limit)))


def problem_22(names: list = ed.get_problem_22_data()) -> int:
    """
    https://projecteuler.net/problem=22
    Using data.get_problem_22_data(), begin by sorting it into alphabetical order.
        Then working out the alphabetical value for each name,
        multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
        is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """
    dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
           "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
           "X": 24, "Y": 25, "Z": 26}
    names = str(names)
    names = names.strip().split(',')
    names = [re.sub(r'\W', '', x) for x in names]
    names.sort()
    r = 0

    for i, v in enumerate(names):
        t = 0
        for x in v:
            t += dic[x]
        r += t * (i + 1)

    return r


def problem_67():
    """
    https://projecteuler.net/problem=67
    Find the maximum total from top to bottom in get_problem_67_data() containing a triangle with one-hundred rows.
    """
    number = ed.get_problem_67_data().strip().split('\n')

    for i in range(1, len(number)):
        number[i] = number[i].strip().split(' ')
        number[i] = [int(x) for x in number[i]]

    number[0] = [59]
    return int(ef.find_max_sum_path(number))
