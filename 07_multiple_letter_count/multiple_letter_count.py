def multiple_letter_count(phrase):
    result = {}
    count = 0
    for char in phrase:
        result[char] = result.get(char, 0) + 1 
    return result
    
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """