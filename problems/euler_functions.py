import math
import random
import string
from collections import Counter
from datetime import date
from functools import lru_cache


def prime_valuation(num):
    prime = [True] * num

    for i in range(2, num):
        if prime[i]:
            yield i
            for x in range(i ** 2, num, i):
                prime[x] = False


def is_prime(num: int) -> bool:
    if num != 1 or num != 0:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return True


def find_prime(num):
    primes = list(prime_valuation(upper_value(num)))
    return primes[num - 1]


def sum_primes(num: int) -> int:
    r, sieve = 0, [True] * num

    for p in range(2, num):
        if sieve[p]:
            r += p
            for i in range(p * p, num, p):
                sieve[i] = False
    return r


def power_less_than(num, multi):
    p = num
    while p < multi:
        p *= num
    return p // num


def smallest_multiple(n: int) -> int:
    multi = 1
    for p in prime_valuation(n + 1):
        multi *= power_less_than(p, n + 1)
    return multi


def sum_squares(num: int) -> int:
    r = 0
    for i in range(num):
        r += i ** 2
    return r


def square_sum(num: int) -> int:
    r = 0
    for i in range(num):
        r = r + i
    return r ** 2


def upper_value(num):
    if num < 6:
        return 100
    return math.ceil(num * (math.log(num) + math.log(math.log(num))))


def generate_num(length: int = 1) -> int:
    num = ''
    return int(num.join(random.choice(string.digits) for i in range(length)))


def convert_to_list(num: int) -> list:
    digits = []
    for i in str(num):
        digits.append(i)

    return digits


def get_greatest_product_in_grid(numbers: list) -> int:
    product_current = 0

    # diagonal-right
    index_outer = 0
    index_inner = 0

    while index_outer < 17:
        for i in range(1, 18):
            num1 = numbers[index_outer][index_inner]
            num2 = numbers[index_outer + 1][index_inner + 1]
            num3 = numbers[index_outer + 2][index_inner + 2]
            num4 = numbers[index_outer + 3][index_inner + 3]
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
            num1 = numbers[index_outer][index_inner]
            num2 = numbers[index_outer - 1][index_inner + 1]
            num3 = numbers[index_outer - 2][index_inner + 2]
            num4 = numbers[index_outer - 3][index_inner + 3]
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
            num1 = numbers[index_outer][index_inner]
            num2 = numbers[index_outer][index_inner + 1]
            num3 = numbers[index_outer][index_inner + 2]
            num4 = numbers[index_outer][index_inner + 3]
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
            num1 = numbers[index_outer][index_inner]
            num2 = numbers[index_outer + 1][index_inner]
            num3 = numbers[index_outer + 2][index_inner]
            num4 = numbers[index_outer + 3][index_inner]
            product = num1 * num2 * num3 * num4
            if product_current < product:
                product_current = product
            index_inner += 1
        index_outer += 1
        index_inner = 0

    return product_current


def get_divisors(num: int) -> list:
    divs = [1]

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divs.extend([int(i), int(num / i)])

    return list(set(divs))


@lru_cache(maxsize=None)
def get_path_results(length: int, width: int) -> int:
    """
    Return max number of routes from (x, y) to (l, w) in a grid.
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


def get_num_dates(start_year: int, end_year: int) -> Counter:
    counter = Counter()

    for year in range(start_year, end_year):
        for month in range(1, 13):
            day = date(year, month, 1)
            counter[day.weekday()] += 1

    return counter[6]


def factorial(num: int) -> int:
    return math.factorial(num)


def find_amicable(limit: int) -> list:
    primes = []
    for i in range(limit):
        if is_prime(i):
            primes.append(i)
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
