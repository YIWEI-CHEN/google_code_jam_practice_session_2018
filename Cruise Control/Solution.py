#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:18:09 2018

@author: yiwei
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 06:11:18 2018

@author: yiwei
"""
from copy import deepcopy
from collections import namedtuple

class Horse(object):
    def __init__(self, location, speed):
        self.location = location
        self.speed = speed
    def __str__(self):
        return 'Horse(' + ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()]) + ')'

def str_list(l):
    return ('[' + ', '.join(str(e) for e in l) + ']')

def calculate_speed(destination, horse_list, collapse_time):
    # print(collapse_time, str_list(horse_list))
    num_horses = len(horse_list)
    if num_horses == 1:
        horse = horse_list[0]
        t_dest = (destination - horse.location) / horse.speed
        total_time = t_dest + collapse_time
        return round(destination / total_time, 6)

    fastest_horse = max(horse_list, key=lambda h: h.speed)
    idx = horse_list.index(fastest_horse)
    if idx == num_horses - 1:
        horse_list.pop(idx)
    else:
        next_horse = horse_list[idx + 1]
        t_catch = (next_horse.location - fastest_horse.location) / (fastest_horse.speed - next_horse.speed)
        location_catch = next_horse.location + next_horse.speed * t_catch
        if location_catch <= destination:
            collapse_time += t_catch
            horse_list.pop(idx + 1)
            for horse in horse_list:
                horse.location = horse.location + horse.speed * t_catch
            fastest_horse.speed = next_horse.speed
        else:
            for i in range(idx + 1  , num_horses):
                horse_list.pop(i)
    return calculate_speed(destination, horse_list, collapse_time)

if __name__ == '__main__':
    TestCase = namedtuple('TestCase', ['destination', 'num_horses', 'answer'])
    HorseStaus = namedtuple('HorseStaus', ['initial_position', 'max_speed', ])

    FROM_STDIN = True
    # FROM_STDIN = False

    testcases = list()
    data = (
        (2525, 1, 101.000000, 2400, 5),
        (100, 2, 33.333333, 80, 100, 70, 10), # j > i, Si < Sj
        (300, 2, 100.000000, 120, 60, 60, 90), # j > i, Si > Sj, Dcatch < D
        (210, 2, 126.000000, 120, 60, 60, 90), # j > i, Si > Sj, Dcatch > D
        (240, 2, 120.000000, 120, 60, 60, 90), # j > i, Si > Sj, Dcatch == D
        (330, 3, 11.000000, 90, 30, 30, 10, 60, 60), # k > j > i, Sj > Sk > Si
        (330, 3, round(330/24, 6), 90, 10, 30, 30, 60, 60), # k > j > i, Sj > Sk, Si > Sk, Dmatch_ijk < D
        (108, 3, round(108/2.6, 6), 90, 10, 30, 30, 60, 60), # k > j > i, Sj > Sk, Si > Sk, Dmatch_ijk > D
    )
    for case in data:
        testcases.append(TestCase._make(case[:3]))
    
    NUM_TESTCASES = len(testcases)

    t = int(input()) if FROM_STDIN else NUM_TESTCASES
    
    for i in range(1, t+1):
        horse_list = []
        destination, num_horses = list(map(int, input().split(' '))) if FROM_STDIN else testcases[i - 1][0:2]
        collapse_time = 0
        # Parse horse status
        for h in range(num_horses):
            start = 3 + h * 2
            location, speed = list(map(int, input().split(' '))) if FROM_STDIN else data[i - 1][start: start+2]
            horse_list.append(Horse(location, speed))
            horse_list.sort(key=lambda h: h.location)
            # ori_horse_list = deepcopy(horse_list)

        output = calculate_speed(destination, horse_list, collapse_time)
        if FROM_STDIN:
            print("Case #{}: {}".format(i, output))
        else:
            ans = testcases[i - 1].answer
            result = 'pass' if ans == output else 'failed'
            print("Case #{}: {}\t{} ({})".format(i, output, result, destination))

