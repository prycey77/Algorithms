import pytest
from word_in_string import find_balloons

def test_balloon_in_one():
    res = find_balloons('BALLOONS')
    assert res == 1

def test_ball_is_zero():
    res = find_balloons('BALL')
    assert res == 0

def test_ballxxoons_is_one():
    res = find_balloons('BALLXXOONS')
    assert res == 1

def test_balloonsballoons_is_two():
    res = find_balloons('BALLOONSBALLOONS')
    assert res == 2