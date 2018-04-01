#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 06:11:18 2018

@author: yiwei
"""
import math

NUM_TWO_END_STALLS = 2

threshold_table = {
    0: 0,
    1: 0,
    2: 1,
    # 3: 1,
    # 4: 2,
}

def get_threshold(num_stalls):
    if num_stalls in threshold_table:
        return threshold_table[num_stalls]

    one = math.ceil((num_stalls - 1) / 2)
    the_other = num_stalls - 1 - one
    threshold_table[num_stalls] = get_threshold(one) + get_threshold(the_other) + 1
    return threshold_table[num_stalls]
    
def measure_empty_distances(left, right):
    middle = (left + right) // 2
    left_empty_distance = middle - left - 1
    right_empty_distance = right - middle - 1
#    if left_empty_distance < 0 or right_empty_distance < 0:
#        print('left:{}, right:{}, middle:{}'.format(left, right, middle))
    return middle, min(left_empty_distance, right_empty_distance), max(left_empty_distance, right_empty_distance)

def calcuate_empty_stalls(stalls, people):
    if people >= stalls or stalls == 0 or people == 0:
        return (0, 0)

    # if people > get_threshold(stalls):
    #     return (0, 0)

    # leftmost and rightmost stalls constantly occupied by bathroom guard.
    total_stalls = stalls + NUM_TWO_END_STALLS
    occupied_positions = [0, total_stalls - 1]

    # people choose a stall
    for enter_time in range(people):
        current_min, current_max, selected = -1, -1, None

        for i, pos in enumerate(occupied_positions[:-1]):
            left = pos
            right = occupied_positions[i + 1]

            # no middle point between two consecutive integers
            if right - left == 1:
                continue

            middle, min_dist, max_dist = measure_empty_distances(left, right)
            if min_dist > current_min:
                current_min, current_max, selected= min_dist, max_dist, middle
            elif min_dist == current_min:
                if max_dist > current_max:
                    current_min, current_max, selected= min_dist, max_dist, middle

        if selected is not None:
            occupied_positions.append(selected)
            occupied_positions.sort()
            # print(occupied_positions)

    if selected is None:
        return (0, 0)
    else:
        return (current_max, current_min)

if __name__ == '__main__':
    from collections import namedtuple
    TestCase = namedtuple('TestCase', ['num_other_stalls', 'num_people', 'answer'])

    FROM_STDIN = True
    # FROM_STDIN = False
    # for i in [100]:
    #     print('{}: {}'.format(i, get_threshold(i)))

    testcases = list()
    for case in (
        (4, 2, (1, 0)),
        (5, 2, (1, 0)),
        (5, 3, (1, 0)),
        (5, 4, (0, 0)),
        (6, 1, (3, 2)),
        (6, 2, (1, 1)),
        (6, 3, (1, 0)),
        (7, 1, (3, 3)),
        (7, 2, (1, 1)),
        (7, 3, (1, 1)),
        (7, 4, (0, 0)),
        (7, 5, (0, 0)),
        (7, 6, (0, 0)),
        (8, 1, (4, 3)),
        (8, 2, (2, 1)),
        (8, 3, (1, 1)),
        (8, 4, (1, 0)),
        (9, 5, (1, 0)),
        (9, 6, (0, 0)),
        (19, 12, (0, 0)),
        (20, 13, (0, 0)),
        (100, 64, (0, 0)),
        (100, 65, (0, 0)),
        (1000, 1000, (0, 0)),
        (1000, 1, (500, 499)),
    ):
        testcases.append(TestCase._make(case))

    NUM_TESTCASES = len(testcases)

    t = int(input()) if FROM_STDIN else NUM_TESTCASES

    for i in range(1, t+1):
        num_other_stalls, num_people = list(map(int, input().split(' '))) if FROM_STDIN else testcases[i - 1][0:2]
        output = calcuate_empty_stalls(num_other_stalls, num_people)

        if FROM_STDIN:
            print("Case #{}: {} {}".format(i, *output))
        else:
            ans = testcases[i - 1].answer
            result = 'pass' if ans == output else 'failed'
            print("Case #{}: {} {}\t{} (N={}, K={})".format(i, output[0], output[1], result, num_other_stalls, num_people))
