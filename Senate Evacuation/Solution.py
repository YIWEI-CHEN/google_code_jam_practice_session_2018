#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 06:58:23 2018

@author: yiwei
"""
from copy import copy
from itertools import combinations
from string import ascii_uppercase
    
def has_majority(senators):
    total = sum(senators)
    if total == 0:
        return False
    
    half_percent = 0.5
    for num in senators:
        if num / total > half_percent:
            return True
    return False

def is_empty(senators):
    if sum(senators) == 0:
        return True
    return False

def strategy(num_parties, senators, peo_per_time):
    choice_start = 1
    choice_end = peo_per_time + 1
    
    for i, choice in enumerate(range(choice_start, choice_end)):
        for indices in combinations(range(num_parties), choice):
            tmp = copy(senators)
            for idx in indices:
                tmp[idx] -= (peo_per_time - i)
                if tmp[idx] < 0:
                    break
    
            if tmp[idx] < 0:
                continue
    
            yield (indices, tmp)

def get_instruction(indices, peo_per_time):
    if len(indices) == 1 and peo_per_time == 2:
        indices = (indices[0], indices[0])
    return ''.join(ascii_uppercase[i] for i in indices)

def evacuation(num_parties, senators):
    if is_empty(senators):
        return ''
    
    for peo_per_time in range(2, 0, -1):
        for indices, evacuated_result in strategy(num_parties, senators, peo_per_time):
            if has_majority(evacuated_result):
                continue
            
            instruction = get_instruction(indices, peo_per_time)
#            print(instruction, evacuated_result)
            if is_empty(evacuated_result):
                return instruction
            else:
                next_instruction = evacuation(num_parties, evacuated_result)
                return '{} {}'.format(instruction, next_instruction)
            

if __name__ == '__main__':
    t = int(input())
    
    for i in range(1, t+1):
        num_parties = int(input())
#        num_parties = 3
        senators = list(map(int, input().split(' ')))
#        senators = [2, 3, 1]
        
        ans = evacuation(num_parties, senators)
        #ans = answer_map[tuple([num_parties] + senators)]
        print("Case #{}: {}".format(i, ans))
