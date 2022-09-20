#!/usr/bin/env python
import pytest
import requests

# Exercise 1
def divide(x,y):
    return (x/y)

# Exercise 2
def test_6_div_1_is_6():
    assert divide(6,1) == 6

# Exercise 3
def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(1/0)

# Exercise 4
@pytest.fixture
def wordle_words():
     req = requests.get('https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/ca9018b32e963292473841fb55fd5a62176769b5/valid-wordle-words.txt')
     return req.text.splitlines()

def test_first_word(wordle_words):
    assert wordle_words[0] == "aahed"

def test_last_word(wordle_words):
    assert wordle_words[-1] == "zymic"


