def extract_full_names(people):
    result = []
    for name in people:
        first_name = name['first']
        last_name = name['last']
        full_name = first_name +' ' + last_name
        result.append(full_name)
    print (result)
names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'}]
extract_full_names(names)
    # """Return list of names, extracting from first+last keys in people dicts.

    # - people: list of dictionaries, each with 'first' and 'last' keys for
    #           first and last names

    # Returns list of space-separated first and last names.

    #     >>> names = [
    #     ...     {'first': 'Ada', 'last': 'Lovelace'},
    #     ...     {'first': 'Grace', 'last': 'Hopper'},
    #     ... ]

    #     >>> extract_full_names(names)
    #     ['Ada Lovelace', 'Grace Hopper']
    # """