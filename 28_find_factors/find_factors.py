def find_factors(num):
    n = 1
    result = []
    while( n <= num):
        if (num % n == 0):
            result.append(n)
        n += 1
    return result
find_factors(10)

    # """Find factors of num, in increasing order.

    # >>> find_factors(10)
    # [1, 2, 5, 10]

    # >>> find_factors(11)
    # [1, 11]

    # >>> find_factors(111)
    # [1, 3, 37, 111]

    # >>> find_factors(321421)
    # [1, 293, 1097, 321421]
    # """
