#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 14:04:13 2018

@author: yiwei
"""
import json
import unittest
from itertools import combinations

from Solution import evacuation

NUM_PARTIES = 10
NUM_PARTIES = 3
TOTAL_NUM_SENATES = 40
TOTAL_NUM_SENATES = 6

# NUM_PARTIES = 10, TOTAL_NUM_SENATES = 40, the create_senates will take much time 
MAX_PEOPLE_PER_TIME = 2

def pretty_json(obj, default=lambda o: o.__dict__):
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False, default=default)

def create_senates(num_parties, total_num_senates):
    """
        X1 + X2 + ... + Xn = total_num_senates, Xi >= 1
    """
    combs = combinations(range(total_num_senates - 1), num_parties - 1)
    for comb in combs:
        skip = False
        senates_dist = []
        # print(comb)
        for i, flag in enumerate(comb):
            if i == 0:
                senates_dist.append(flag - (-1))
            if i == len(comb) - 1:
                senates_dist.append(total_num_senates - 1 - flag)
            else:
                senates_dist.append(comb[i+1] - flag)
            if abs(senates_dist[i+1] - senates_dist[i]) > MAX_PEOPLE_PER_TIME:
                skip = True
                break
        if skip:
            continue
        else:
            # print(senates_dist)
            yield senates_dist
            

class TestSenateEvacuation(unittest.TestCase):
    """
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_evacuation(self):
        num_parties = NUM_PARTIES
        total_senates = TOTAL_NUM_SENATES
        print()
        for senates in create_senates(num_parties, total_senates):
            ans = evacuation(num_parties, senates)
            print('{}: {}'.format(senates, ans))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestSenateEvacuation))
