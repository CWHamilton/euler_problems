import re
from functools import reduce

import problems.common as ef


def problem_1(num_1: int, num_2: int, limit: int) -> int:
    """
    :param num_1:   Number 1 to divide by
    :param num_2:   Number 2 to divide by
    :param limit:   Max limit to check for numbers that divide by num_1 and/or num_2
    :return:
    """
    r = 0

    for i in range(limit):
        if i % num_1 == 0 or i % num_2 == 0:
            r += i
    return r


def problem_2(limit: int) -> int:
    """
    :param limit:   Max limit of numbers to check
    :return:
    """
    a, b, r = 1, 1, 0

    while b <= limit:
        c = b
        b = b + a
        a = c

        if b % 2 == 0:
            r += b

    return r


def problem_3(num: int) -> int:
    """
    :param num:       Number to find the largest prime factor of
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


def problem_5(n_min: int, n_max: int) -> int:
    """
    :param n_min:     Minimum multiplier
    :param n_max:     Maximum multiplier
    :return:
    """
    return ef.smallest_multiple(n_min=n_min, n_max=n_max)


def problem_6(limit: int) -> int:
    """
    :param limit:     Max number to count sums for
    :return:
    """
    return ef.square_sum(limit) - ef.sum_squares(limit)


def problem_7(num: int) -> int:
    """
    :param num:       Number of primes to count
    :return:
    """
    return ef.find_nth_prime(num)


def problem_8(num: str, adjacent: int) -> int:
    """
    :param num:         Number to check
    :param adjacent:    Number of adjacent numbers to search for in num with greatest product
    :return:
        number, adj = 12345678, 3
          -> (8*7*6)
            -> 336
    """
    max_v = 0

    for (i, n) in enumerate(num):
        value = reduce((lambda x, y: x * y), map(int, (num[i : i + adjacent])))

        if value > max_v:
            max_v = value

    return max_v


def problem_9(c: int) -> int:
    """
    :param c:     Final value of what a + b + c should equal
    :return:
    """
    for num in range(1, c):
        for a in range(num, c - num):
            b = c - num - a
            if num * num + a * a == b * b:
                return num * a * b


def problem_10(num: int) -> int:
    """
    :param num:     The number to find all primes below
    :return:
        ef.sum_primes(10)
            -> sum(0, 1, 2, 3, 5, 7)
                -> return 18
    """
    return ef.sum_primes(num)


def problem_11(grid: list[list[int]]) -> int:
    """
    :param grid:    A list of numbers to check for adjacent values
    :return:
    """
    return ef.get_greatest_product_in_grid(grid)


def problem_12(expected_divs: int) -> int:
    """
    :param expected_divs:   Number of divisors expected in a number triangle
    :return:

        problem_12(expected_divs=6) --> 6 ({1: [1], 3: [1,3], 6: [1,2,3,6]})
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


def problem_13(nums: list, num_digits: int) -> int:
    """
    :param nums:        List of numbers to sum
    :param num_digits:  Number of digits to return from the sum of nums
    :return:
    """
    num_sum = 0
    for i in nums:
        num_sum += i

    return int(str(num_sum)[0:num_digits])


def problem_14(limit: int):
    """
    :param limit:   Max value to search through
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


def problem_15(length: int, width: int) -> int:
    """
    :param length:  X axis of grid
    :param width:   Y axis of grid
    :return:
    """
    return ef.get_path_results(length=length, width=width)


def problem_16(num: int, power: int) -> int:
    """
    :param num:     Starting number
    :param power:   Exponential number
    :return:

        problem_16(num=2, power=4) --> 7 (sum(1, 6))
    """
    return sum([int(i) for i in str(num ** power)])


def problem_17() -> int:
    """
    :return:

        sum("ninetynine", "onehundred", "onehundredandone") --> 36 (sum([10, 10, 16]))
    """
    dic = {n: 0 for n in range(0, 1001)}

    # Set all unique words used in all numbers from 'zero' to 'one thousand'
    dic[0] = 0  # ''
    dic[1] = len("one")
    dic[2] = len("two")
    dic[3] = len("three")
    dic[4] = len("four")
    dic[5] = len("five")
    dic[6] = len("six")
    dic[7] = len("seven")
    dic[8] = len("eight")
    dic[9] = len("nine")
    dic[10] = len("ten")
    dic[11] = len("eleven")
    dic[12] = len("twelve")
    dic[13] = len("thirteen")
    dic[14] = len("fourteen")
    dic[15] = len("fifteen")
    dic[16] = len("sixteen")
    dic[17] = len("seventeen")
    dic[18] = len("eighteen")
    dic[19] = len("nineteen")
    dic[20] = len("twenty")
    dic[30] = len("thirty")
    dic[40] = len("forty")
    dic[50] = len("fifty")
    dic[60] = len("sixty")
    dic[70] = len("seventy")
    dic[80] = len("eighty")
    dic[90] = len("ninety")

    for i in range(21, 100):
        tens = int(i / 10) * 10
        ones = i - tens
        dic[i] = dic[tens] + dic[ones]

    for i in range(100, 1000):
        hundreds = int(i / 100)
        tens_ones = i - hundreds * 100

        if tens_ones == 0:
            dic[i] = dic[hundreds] + len("hundred")
        else:
            dic[i] = dic[hundreds] + len("hundredand") + dic[tens_ones]

    dic[1000] = len("onethousand")

    return sum(dic.values())


def problem_18(numbers: list) -> int:
    """
    :param numbers:     Numbers triangle
    :return:
    """
    for i in range(1, len(numbers)):
        numbers[i] = numbers[i]
        numbers[i] = [int(x) for x in numbers[i]]

    numbers[0] = [75]

    return int(ef.find_max_sum_path(numbers))


def problem_19(start_year: int, end_year: int) -> int:
    """
    :param start_year:  Earliest Year
    :param end_year:    End Year
    :return:
    """
    return int(str(ef.get_num_dates(start_year=start_year, end_year=end_year)))


def problem_20(number: int) -> int:
    """
    :param number:  Int value to get factorial for
    :return:
    """
    return sum([int(i) for i in str(ef.factorial(number))])


def problem_21(limit: int) -> int:
    """
    :param limit:   Find list of amicable numbers up to limit
    :return:
    """
    return int(sum(ef.find_amicable(limit=limit)))


def problem_22(names: list) -> int:
    """
    :param names:   List of names to use
    :return:
    """
    dic = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    names = str(names)
    names = names.strip().split(",")
    names = [re.sub(r"\W", "", x) for x in names]
    names.sort()
    r = 0

    for i, v in enumerate(names):
        t = 0
        for x in v:
            t += dic[x]
        r += t * (i + 1)

    return r


def problem_23(limit: int) -> int:
    """
    :param limit:       Max number that can't be written as the sum of two abundant numbers
    :return:
    """
    ab_limit = limit
    ab_nums = [i for i in range(12, ab_limit) if sum(ef.get_divisors(i)) > i]

    non_abundant_sums = [x for x in range(ab_limit)]

    for i in range(len(ab_nums)):
        for j in range(i, ab_limit):
            if ab_nums[i] + ab_nums[j] < ab_limit:
                non_abundant_sums[ab_nums[i] + ab_nums[j]] = 0
            else:
                break

    return sum(non_abundant_sums)


def problem_24(perm: int, chars: str) -> int:
    """
    :param perm:        Permutation index to find
    :param chars:       Number of characters to use
    :return:
    """
    return int(ef.get_permutations(permutation=perm, chars=chars))


def problem_25(count: int) -> int:
    """
    :param count:       Once number of characters is hit, return index
    :return:
    """
    a, b, c = 1, 1, 2
    fib_list = [a, b, c]

    while len(str(b)) < count:
        b = a + b
        a = c
        c = b
        fib_list.append(b)

    return len(fib_list) - 1


def problem_26(limit: int) -> int:
    """
    :param limit:       Max value to search
    :return:
    """
    primes = ef.sieve(limit)
    d = {n: 0 for n in range(1, limit)}

    d[3] = 1

    for i in primes[3:]:
        d[i] = len(ef.recurring_decimal(i))

    for i in range(6, limit):
        if not d[i]:
            if i % 2 != 0 != i % 5:
                for j in primes:
                    if i % j == 0:
                        num1 = d[j]
                        num2 = d[i / j]
                        d[i] = ef.lowest_common_multiplier(num2, num1)
                        break
            else:
                number = i
                while number % 2 == 0:
                    number = number / 2
                while number % 5 == 0:
                    number = number / 5
                d[i] = d[number]

    return list(d.values()).index(max(d.values())) + 1


def problem_27() -> int:
    # I don't know what half of those words mean.
    pass


def problem_28(limit: int) -> int:
    """
    :param limit:       Max grid spiral size
    :return:
    """
    # Last number in limit x limit spiral grid
    numbers = limit * limit

    # All values on a diagonal axis in a spiral grid are odd.  Can skip even numbers.
    odd_numbers = range(1, numbers + 1, 2)

    """
    The odd values on the diagonal axis follow a pattern of skipping numbers.
    Number of skipped values between each value: 
        0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4, etc.
    The number of skipped values increases every 4 digits.
    """
    i, skip, solution = 0, 1, 1

    while odd_numbers[i] != numbers:
        for n in range(4):
            i += skip
            solution += odd_numbers[i]
        skip += 1

    return solution


def problem_29(num: int) -> int:
    """
    :param num:       Number of values to search through for a^b where a and b are range(2, num+1)
    :return:
    """
    return len(set([a ** b for b in range(2, num + 1) for a in range(2, num + 1)]))


def problem_67(numbers: list) -> int:
    """
    :param numbers:     Numbers triangle
    :return:
    """
    for i in range(1, len(numbers)):
        numbers[i] = numbers[i]
        numbers[i] = [int(x) for x in numbers[i]]

    numbers[0] = [59]
    return int(ef.find_max_sum_path(numbers))
