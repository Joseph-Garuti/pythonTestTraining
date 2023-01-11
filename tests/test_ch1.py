#Write a function that takes a string argument
#and returns the number of vowels


def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count


def digit_count(string):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    for char in string:
        if char in digits:
            count += 1
    return count


def special_char_count(string):
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '<', '>', ',', '.', '/', '?',
                     ';', ':', '[', ']', '{', '#', '\\', '|', '\'', '\"']
    count = 0
    for char in string:
        if char in special_chars:
            count += 1
    return count


def space_count(string):
    spaces = ' '
    count = 0
    for char in string:
        if char == spaces:
            count += 1
    return count


def test_with_my_name():
    assert vowel_count('joseph garuti') == 5


def test_with_my_uppercase_name():
    assert vowel_count('JOSEPH GARUTI') == 5


def test_with_digits():
    assert digit_count('j0seph Garut1') == 2


def test_with_special_chars():
    assert special_char_count('J\\o$\'ep# G@\'ru\"t\"! -') == 10


def test_spaces():
    assert space_count('Joseph Garuti Jr') == 2


def tests():
    test_with_my_name()
    test_with_my_uppercase_name()
    test_with_digits()
    test_with_special_chars()
    test_spaces()

