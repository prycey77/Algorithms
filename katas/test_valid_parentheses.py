import pytest
from valid_parentheses import is_valid

def test_check_two_brackets_is_true():
    res = '()'
    assert is_valid(res) == True

def test_check_one_bracket_is_false():
    res = '('
    assert is_valid(res) == False

def test_check_multipul_correct_brackets_is_true():
    res = '(){}[]'
    assert is_valid(res) == True

def test_check_even_number_of_brackets_in_wrong_place_is_false():
    res = '({)}'
    assert is_valid(res) == False