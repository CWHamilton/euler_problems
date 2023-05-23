import math
from collections import Counter
from collections.abc import Iterable
from datetime import date
from functools import lru_cache
from itertools import permutations as perm


"""
Some of these common methods will only have use in one test, but may be used in future.  
Values in those methods might be slightly more hard-coded than I'd like, but they so far serve their purpose.
"""


def prime_valuation(num: int) -> Iterable:
    """
    Evaluates all numbers from 0 to num and identifies whether they are prime

    :param num:     Number to evaluate
    :return:

    Examples:
    ---------
        >>> prime_valuation(6)
            [True, True, True, True, False, True, False]
    """
    prime = [True] * num

    for i in range(2, num):
        if prime[i]:
            yield i
            for x in range(i**2, num, i):
                prime[x] = False


def identify_prime(num: int) -> bool:
    """
    Identifies whether a specific number is prime

    :param num:     Number to identify whether it is prime or not
    :return:

    Examples:
    ---------
        >>> identify_prime(4)
            False
        >>> identify_prime(5)
            True
    """
    if num not in [0, 1]:  # 0 and 1 are considered prime numbers, skip and return True
        for i in range(2, num):
            if num % i == 0:
                return False  # num has a divisor beyond 1 and itself and is therefore not prime, return False
        else:
            return True  # num has no divisors except 1 and itself, return True.
    else:
        return True


def find_nth_prime(num: int) -> int:
    """
    Loops through all primes and returns the nth prime value

    :param num:     Returns the nth prime
    :return:

    Examples:
    ---------
        >>> find_nth_prime(n=4)
            7
    """
    return list(prime_valuation(upper_bound_nth_prime(num)))[num - 1]


def sum_primes(limit: int) -> int:
    """
    Sum all the primes from 0 to limit

    :param limit:
    :return:

    Examples:
    ---------
        >>> sum_primes(num=10)
            17
        >>> sum_primes(2)
            2
    """
    r, s = 0, [True] * limit

    for p in range(2, limit):
        if s[p]:
            r += p
            for i in range(p * p, limit, p):
                s[i] = False
    return r


def sieve(limit: int) -> list:
    """
    Sieve of Eratosthenes
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    :param limit:       Finds all primes up to given limit
    :return:

    Examples:
    ---------
            >>> sieve(limit=10)
                [2, 3, 5, 7]
    """
    p = [True] * limit
    p[0], p[1] = False, False

    for i in range(2, int(limit**0.5 + 1)):
        index = i * 2
        while index < limit:
            p[index] = False
            index = index + i

    return [i for i in range(limit) if p[i]]


def power_less_than(num: int, limit: int) -> int:
    """
    Returns the lowest num**n product under limit

    :param num:     Number to multiply
    :param limit:   Number to not go over
    :return:        num**n

    Examples:
    ---------
        >>> power_less_than(num=2, limit=20)
            16 (2**4 = 16, highest without going over 20)
        >>> power_less_than(num=2, limit=40)
            32 (2**5 = 32, highest without going over 40)
        >>> power_less_than(num=3, limit=20)
            9  (3**2 =  9, highest without going over 20)
        >>> power_less_than(num=3, limit=30)
            27 (3**3 = 27, highest without going over 30)
    """
    p = num
    while p < limit:
        p *= num
    return p // num


def smallest_multiple(n_min: int, n_max: int) -> int:
    """
    Returns the smallest number that is evenly divisible by all the numbers between n_min and n_max

    :param n_min:   Minimum value
    :param n_max:   Maximum value
    :return:

    Examples:
    ---------
        >>> smallest_multiple(n_min=1, n_max=4)
            12 (first number divisible by 1, 2, 3, 4)
        >>> smallest_multiple(n_min=2, n_max=5)
            60 (first number divisible by 2, 3, 4, 5)
    """
    multi = n_min
    for p in prime_valuation(n_max + 1):
        multi *= power_less_than(p, n_max + 1)
    return multi


def sum_squares(limit: int) -> int:
    """
    Sums all square values in range 0 > limit

    :param limit:     Range to use
    :return:

    Examples:
    ---------
        >>> sum_squares(limit=3)
            17 (sum[0**2, 1**2, 2**2, 3**2])
    """
    return sum([i**2 for i in range(limit)])


def square_sum(limit: int) -> int:
    """
    Sums a range and returns the squared value

    :param limit:   Range to use
    :return:

    Examples:
    ---------
        >>> square_sum(limit=5)
            100 (sum[0, 1, 2, 3, 4] ** 2)
    """
    return sum([i for i in range(limit)]) ** 2


def upper_bound_nth_prime(num: int) -> int:
    """
    There is a known upper bound to prime.  This method returns the upper bound value for num
    https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime

    :param num:     Number to return upper bounds for
    :return:
    """
    if num < 6:
        return 100
    return math.ceil(num * (math.log(num) + math.log(math.log(num))))


def get_greatest_product_in_grid(grid: list[list[int]]) -> int:
    """
    Will find the greatest product of four adjacent numbers in a 20x20 grid

    :param grid:    Grid to search through
    :return:
    """
    product_current = 0

    # diagonal-right
    index_outer = 0
    index_inner = 0

    while index_outer < 17:
        for i in range(1, 18):
            num1 = grid[index_outer][index_inner]
            num2 = grid[index_outer + 1][index_inner + 1]
            num3 = grid[index_outer + 2][index_inner + 2]
            num4 = grid[index_outer + 3][index_inner + 3]
            product = num1 * num2 * num3 * num4
            if product_current < product:
                product_current = product
            index_inner += 1
        index_outer += 1
        index_inner = 0

    # diagonal-left
    index_outer = 3
    index_inner = 0

    while index_outer < 20:
        for i in range(1, 18):
            num1 = grid[index_outer][index_inner]
            num2 = grid[index_outer - 1][index_inner + 1]
            num3 = grid[index_outer - 2][index_inner + 2]
            num4 = grid[index_outer - 3][index_inner + 3]
            product = num1 * num2 * num3 * num4
            if product_current < product:
                product_current = product
            index_inner += 1
        index_outer += 1
        index_inner = 0

    # horizontal
    index_outer = 0
    index_inner = 0

    while index_outer < 20:
        for i in range(1, 18):
            num1 = grid[index_outer][index_inner]
            num2 = grid[index_outer][index_inner + 1]
            num3 = grid[index_outer][index_inner + 2]
            num4 = grid[index_outer][index_inner + 3]
            product = num1 * num2 * num3 * num4
            if product_current < product:
                product_current = product
            index_inner += 1
        index_outer += 1
        index_inner = 0

    # vertical
    index_outer = 0
    index_inner = 0

    while index_outer < 17:
        for i in range(1, 21):
            num1 = grid[index_outer][index_inner]
            num2 = grid[index_outer + 1][index_inner]
            num3 = grid[index_outer + 2][index_inner]
            num4 = grid[index_outer + 3][index_inner]
            product = num1 * num2 * num3 * num4
            if product_current < product:
                product_current = product
            index_inner += 1
        index_outer += 1
        index_inner = 0

    return product_current


def get_divisors(num: int) -> list:
    """
    Returns all divisors for a number

    :param num:
    :return:

    Examples:
    ---------
        >>> get_divisors(num=6)
            [1, 2, 3, 6]
    """
    divs = [1]  # 1 will always be a divisor

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divs.extend([int(i), int(num / i)])

    return list(set(divs))


@lru_cache(maxsize=None)
def get_path_results(length: int, width: int) -> int:
    """
    Return max number of routes from (0, 0) to (l, w) in a grid.

    :param length:  Grid length
    :param width:   Grid width
    :return:

        get_path_results(length: 2, width: 2)
            6
        https://projecteuler.net/project/images/p015.png
    """
    if length > width:
        return get_path_results(width, length)
    elif length == 0:
        return 1
    else:
        return get_path_results(length - 1, width) + get_path_results(length, width - 1)


def find_max_sum_path(nums: list) -> int:
    sum_total = 0

    for i in range(len(nums) - 2, -1, -1):
        for v in range(len(nums[i])):
            nums[i][v] = nums[i][v] + max(nums[i + 1][v], nums[i + 1][v + 1])
            sum_total += 1
        nums.pop()

    return int(nums[0][0])


def get_num_dates(start_year: int, end_year: int) -> int:
    """
    Returns the number of times Sunday fell on the 1st of the month in a given set of years

    :param start_year:  Year to start search
    :param end_year:    Last year to search
    :return:

    Examples:
    ---------
        >>> get_num_dates(start_year=2000, end_year=2001)
            1 (int("<number of Sundays in the year 2000 that are on the 1st of the month>"))
    """
    counter = Counter()

    for year in range(start_year, end_year):
        for month in range(1, 13):
            day = date(year, month, 1)
            counter[day.weekday()] += 1

    return counter[6]


def factorial(num: int) -> int:
    """
    Returns the product of all positive integers less than or equal to given num.

    :param num:     num!
    :return:

    Examples:
    ---------
        >>> factorial(num=2)
            2
        >>> factorial(num=4)
            24
        >>> factorial(num=8)
            40320
    """
    return math.factorial(num)


def find_amicable(limit: int) -> list:
    """
    Returns list of amicable numbers.
    Amicable numbers are two different numbers where the sum of their divisors equals the other number, eg:
        220 sum[1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110] = 284
        284 sum[1, 2, 4, 71, 142] = 220

    :param limit:   Max number to check for amicable
    :return:

    Examples:
    ---------
        >>> find_amicable(limit=1500)
            [220, 284, 1210, 1184]
    """
    primes = [i for i in range(limit) if identify_prime(i)]
    amicable = []
    checked = []

    for i in range(2, limit):
        if i not in primes and i not in checked:
            a = sum(get_divisors(i))
            b = sum(get_divisors(a))
            checked.extend([a, b])

            if i == b:
                if a != b:
                    amicable.extend([i, a])

    return amicable


def get_permutations(permutation: int, chars: str) -> str:
    """
    Finds all permutations of chars and returns the permutation index

    :param permutation:     Single indexed permutation to return
    :param chars:           Characters to generate permutations with
    :return:

    Examples:
    ---------
        >>> get_permutations(permutation=3, chars="012")
            102  ([012, 021, 102, 120, 201, 210][2])
    """
    return "".join(list(perm(chars, 10))[permutation - 1])


def recurring_decimal(div: int) -> str:
    """
    Returns the recurring decimals for divisor as a string

    :param div:     Divisor to return decimal values from
    :return:

    Examples:
    ---------
        >>> recurring_decimal(div=3)
            1 (0.33333...)
    """
    if div < 10:
        dividend = 10
    elif 10 <= div < 100:
        dividend = 100
    else:
        dividend = 1000

    value = dividend
    text = ""

    for i in range(div):
        text += str(dividend % div)
        dividend = dividend % div

        if dividend < div:
            dividend *= 10
            if dividend < div:
                dividend *= 10
                text += "0"
                if dividend < div:
                    dividend *= 10
                    text += "0"
        if dividend == value:
            return text
    return text


def greatest_common_denominator(num1: int, num2: int) -> int:
    """
    Return greatest common denominator of two numbers

    :param num1:    First number
    :param num2:    Second number
    :return:

    Examples:
    ---------
        >>> greatest_common_denominator(num1=10, num2=20)
            10  (10*2 = 20, 10*1=10)
        >>> greatest_common_denominator(num1=12, num2=18)
            6   (6*2 = 12, 6*4 = 18)
    """
    r = 1

    while r != 0:
        r = num1 % num2
        num1 = num2
        num2 = r

    return num1


def lowest_common_multiplier(num1: int, num2: int) -> float:
    """
    Return lowest common multiplier

    :param num1:    First number
    :param num2:    Second number
    :return:

    Examples:
    ---------
        >>> lowest_common_multiplier(num1=10, num2=20)
            20  ((10*20)/10)
        >>> lowest_common_multiplier(num1=12, num2=18)
            36  ((12*18)/6)
    """
    return (num1 * num2) / greatest_common_denominator(num1, num2)
