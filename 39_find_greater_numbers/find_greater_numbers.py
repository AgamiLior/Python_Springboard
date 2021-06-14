def find_greater_numbers(nums):
    n = 0
    count = 0
    while (n < len(nums)):
        if nums[n] < nums[n+1]:
            count += 1
            n += 1 
    print(count)
find_greater_numbers([1, 2, 3])
find_greater_numbers([5, 4, 3, 2, 1])
    # """Return # of times a number is followed by a greater number.

    # For example, for [1, 2, 3], the answer is 3:
    # - the 1 is followed by the 2 *and* the 3
    # - the 2 is followed by the 3

    # Examples:

    #     >>> find_greater_numbers([1, 2, 3])
    #     3

    #     >>> find_greater_numbers([6, 1, 2, 7])
    #     4

    #     >>> find_greater_numbers([5, 4, 3, 2, 1])
    #     0

    #     >>> find_greater_numbers([])
    #     0
    # """