#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 06:11:18 2018

@author: yiwei
"""
import math
from collections import namedtuple, defaultdict

NUM_TWO_END_STALLS = 2

# threshold_table = {
#     0: 0,
#     1: 0,
#     2: 1,
#     # 3: 1,
#     # 4: 2,
# }

"""we need to avoid this way to save time"""
# Distance = namedtuple('Distance', ['max', 'min'])

"""we do not have to think optimization
If I spend much time coming up with the optimization, the thinking way is not correct"""
# def get_threshold(num_stall):
#     if num_stall in threshold_table:
#         return threshold_table[num_stall]

#     one = math.ceil((num_stall - 1) / 2)
#     the_other = num_stall - 1 - one
#     threshold_table[num_stall] = get_threshold(one) + get_threshold(the_other) + 1
#     return threshold_table[num_stall]
    
def measure_empty_distances(stalls):
    """we should save time on corner cases."""
    # if stalls <= 1 :
    #     return Distance(0, 0)

    """we don't care which one is selected"""
    # selected = stalls // 2 if stalls % 2 == 0 else (stalls + 1) // 2 

    """
        we only want to get left and right empty dist.
        r >= l definitely
    """
    l = (stalls - 1) // 2
    r = stalls // 2

    """we don't return (l, r)"""
    return l, r

def calcuate_empty_stalls(stalls, people):
    """We may not prevent corner case"""
    # if people > stalls or stalls == 0 or people == 0:
    #     return Distance(0, 0)

    """We do not need extra optimization"""
    # if people == stalls or people > get_threshold(stalls):
    #     return Distance(0, 0)

    # key = stall size, value = number of the same size of stalls
    stall_candidate = defaultdict(int)
    stall_candidate[stalls] = 1

    while people > 0:
        """Important point!!!
            As long as the stall number is max for current people, we don't care which one is selected and it is left or right
            All we want is left and right empty size
        """
        num_stall = max(stall_candidate) # """keep point"""
        used = min(stall_candidate[num_stall], people)
        people -= used
        stall_candidate[num_stall] -= used
        if stall_candidate[num_stall] == 0: del stall_candidate[num_stall]
        l, r = measure_empty_distances(num_stall)
        stall_candidate[l] += used
        stall_candidate[r] += used

    return (r, l)


if __name__ == '__main__':
    TestCase = namedtuple('TestCase', ['num_other_stalls', 'num_people', 'answer'])

    FROM_STDIN = True
    # FROM_STDIN = False
    # for i in [100]:
    #     print('{}: {}'.format(i, get_threshold(i)))

    testcases = list()
    for case in (
        (2, 1, (1, 0)),
        (3, 1, (1, 1)),
        (3, 2, (0, 0)),
        (4, 2, (1, 0)),
        (5, 2, (1, 0)),
        (5, 3, (1, 0)),
        (5, 4, (0, 0)),
        (6, 1, (3, 2)),
        (6, 2, (1, 1)),
        (6, 3, (1, 0)),
        (6, 4, (0, 0)),
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
