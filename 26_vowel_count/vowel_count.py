def vowel_count(phrase):
    phrase = phrase.lower()
    result = {}
    for char in phrase:
        if char in 'aeiou':
            result[char] = result.get(char, 0) + 1
    print(result)
vowel_count('HOW ARE YOU? i am great!')
    # """Return frequency map of vowels, case-insensitive.

    #     >>> vowel_count('rithm school')
    #     {'i': 1, 'o': 2}
        
    #     >>> vowel_count('HOW ARE YOU? i am great!') 
    #     {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    # """