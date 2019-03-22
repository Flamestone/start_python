# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as comments
"""


def test_dict():
    dictionary = {}
    dictionary['Alex Kobzar'] = '+375291220849'
    dictionary['Vovan Gurov'] = '+375291002547'

    print 'Number of {} is {}'.format('Alex Kobzar', dictionary['Alex Kobzar'])


def test_list():
    lst = []
    lst.append('Artem')
    lst.append('Alex')
    print lst
    print lst[0]
    print lst[1]
    print lst[22125]


def test_string_formation():
    pattern = '[{log_level}] {message}'

    first_arg = 'DEBUG'
    second_arg = 'Hello'

    new_message = pattern.format(log_level=first_arg, message=second_arg)

    assert new_message == '[{}] {}'.format(first_arg, second_arg)


def test_len():
    strings = [
        'Alex',
        'Kobzar',
        "Vovandes",
        """The're a big string"""
    ]

    maxLen = 0
    for string in strings:
        if len(string) > maxLen:
            maxLen = len(string)

    print 'Our max string has {} letters'.format(maxLen)

    assert maxLen == 19


def test_add():
    i = 2
    j = 4

    print '{} == {}'.format(i, j), i == j
    print '{} != {}'.format(i, j), i != j

    print '{} > {}'.format(i, j), i > j
    print '{} < {}'.format(i, j), i < j

    print '{} <= {}'.format(i, j), i <= j
    print '{} >= {}'.format(i, j), i >= j
