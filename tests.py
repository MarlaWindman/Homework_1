import pytest
import main

def test_1_tax_mass():
    list_items = [1,3,5,7]
    total = 17
    num_got = main.mass_tax(list_items)
    assert num_got == total

def test_2_if_goods():
    dec = {'Wic Eligible food': [1,3 ,6,7,8], "Clothing":[9,8,4,3,2]}
    items = main.in_dec(dec)
    assert items =="good"

def test_3_not_goods():
    dec = {'test': [1, 3, 6, 7, 8]}
    items = main.in_dec(dec)
    assert items == None
