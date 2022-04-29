import pytest
import main

def test_1_tax_mass():
    list_items = [1,3,5,7]
    total = 17
    num_got = main.mass_tax(list_items)
    assert num_got == total

def test_2_if_goods():
    dec = {'Wic Eligible food': ["apple","banna" ,"breed"], "Clothing":["shirt","pants"],
           "everything else": ["stuffy","cup"]}
    items = main.in_dec(dec)
    assert items =="good"

def test_3_not_goods():
    dec = {'test': [1, 3, 6, 7, 8]}
    items = main.in_dec(dec)
    assert items == None

def test_4_item_cost():
    items = ["apple","apple"]
    test = main.item_price(items)
    assert test == [4,4]

def test_5_check_state():
    states = ["Massachusetts"]
    test = main.check_state(states)
    assert test == "good"

