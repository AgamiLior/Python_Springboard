def list_check(lst):
    for val in lst:
        if not isinstance(val, list):
            print(False)
    print(True)
    # """Are all items in lst a list?

    #     >>> list_check([[1], [2, 3]])
    #     True

    #     >>> list_check([[1], "nope"])
    #     False
    # """
