# -*- coding: UTF-8 -*-
# File name: test_wine
# Created by JKChang
# 02/11/2020, 21:31
# Tag:
# Description:
import unittest
from unittest import TestCase

from wine import *


class TestWine(TestCase):
    def test_type(self):
        res = get_all_types().sort()
        if res == ['red', 'white', 'rose'].sort():
            print('get all types test passed')
        else:
            print('wrong')

    def test_varietals(self):
        res = get_all_varietals().sort()
        if res == ['Sangiovesse', 'Malvasia_bianca', 'Chardonnay', 'Canaiolo', 'Nebbiolo', 'Zinfandel',
                   'Primitivo'].sort():
            print('get all varietals test passed')
        elif res == ['Sangiovesse', 'Malvasia_bianca', 'Chardonnay', 'Canaiolo', 'Nebbiolo', 'Zinfandel'].sort():
            print('also_called are missing')
        else:
            print('wrong')

    def test_regions(self):
        res = get_all_types().sort()
        if res == ['Piedmont', 'Chablis', 'France', 'Italy', 'Burgundy', 'Puglia'].sort():
            print('get all regions test passed')
        else:
            print('wrong')

    def test_query_all_null(self):
        res = query().sort()
        if res == ['white_wine', 'Chianti_wine', 'Barbaresco', 'red_wine', 'Chablis_wine', 'Barolo', 'Italian_wine',
                   'French_wine']:
            print('query all null test passed')
        else:
            print('wrong')

    def test_query_color_null(self):
        res = query(varietal='Canaiolo', region='Chianti').sort()
        if res == ['Chianti_wine']:
            print('query color null test passed')
        else:
            print('wrong')

    def test_query_varietal_null(self):
        res = query(color='red', region='Piedmont').sort()
        if res == ['Barolo', 'Barbaresco'].sort():
            print('query varietal null test passed')
        else:
            print('wrong')

    def test_query_region_null(self):
        res = query(color='red').sort()
        if res == ['Barolo_Villero_2015', 'red_wine', 'Barbaresco', 'Barolo', 'Chianti_wine'].sort():
            print('query color only passed ')
        elif res == ['red_wine', 'Barbaresco', 'Barolo', 'Chianti_wine'].sort():
            print('Instances are missing')
        else:
            print('wrong')

    def unmatch(self):
        res = query(color='blue')
        if res == []:
            print('unmatch test pass')
        else:
            print('wrong')


if __name__ == "__main__":
    unittest.main()
