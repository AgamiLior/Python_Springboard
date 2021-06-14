def valid_parentheses(parens):
    count_left = 0
    count_right = 0
    for char in parens:
        if char == '(':
            count_left +=1
        elif char == ')':
            count_right +=1
    if count_right == count_left:
        print(True)
    else:
        print(False)

    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """