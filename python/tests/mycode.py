#!/usr/bin/env python
import pytest

def divide(x,y):
    return (x/y)

def test_6_is_even():
    assert divide(6,2) == 3

# Exercise 2
# Your code goes here

def test_6_div_1_is_6():
    assert divide(6,1) == 6

# Exercise 3
# remove the skip decorator
@pytest.mark.skip
def test_divide_by_zero():
    # Exercise 3 Your test code here
    pass

# Exercise 4
# Wordle words are at https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/ca9018b32e963292473841fb55fd5a62176769b5/valid-wordle-words.txt
# define a fixture called wordle_words so that this is only downloaded once

def test_first_word(wordle_words):
    assert wordle_words[0] == "aahed"

def test_last_word(wordle_words):
    assert wordle_words[-1] == "zymic"


