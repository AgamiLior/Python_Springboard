def remove_every_other(lst):
    result =[]
    for val in lst:
        if val % 2 != 0:
            result.append(val)
    print (result)

    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
