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

class Horse(object):
    def __init__(self, location, speed):
        self.location = location
        self.speed = speed
    def __str__(self):
        return 'Horse(' + ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()]) + ')'

def str_list(l):
    return ('[' + '\n '.join(str(e) for e in l) + ']')

def calculate_speed(destination, horse_list, collapse_time):
    horse_list.sort(key=lambda h: h.location)

    # print(collapse_time, str_list(horse_list))
    num_horses = len(horse_list)
    if num_horses == 1:
        horse = horse_list[0]
        t_dest = (destination - horse.location) / horse.speed
        total_time = t_dest + collapse_time
        return destination / total_time

    fastest_horse = max(horse_list, key=lambda h: h.speed)
    idx = horse_list.index(fastest_horse)
    if idx == num_horses - 1:
        horse_list.pop(idx)
    else:
        next_horse = horse_list[idx + 1]
        if next_horse.speed == fastest_horse.speed:
            for i in range(num_horses - 1  , idx, -1):
                horse_list.pop(i)
        else:
            t_catch = (next_horse.location - fastest_horse.location) / (fastest_horse.speed - next_horse.speed)
            location_catch = next_horse.location + next_horse.speed * t_catch
            if location_catch <= destination:
                collapse_time += t_catch
                horse_list.pop(idx + 1)
                for horse in horse_list:
                    horse.location = horse.location + horse.speed * t_catch
                fastest_horse.speed = next_horse.speed
            else:
                for i in range(num_horses - 1  , idx, -1):
                    horse_list.pop(i)

    return calculate_speed(destination, horse_list, collapse_time)

if __name__ == '__main__':
    FROM_STDIN = True
    # FROM_STDIN = False

    horse_list = []

    if FROM_STDIN:
        readline = input
    else:
        name = 'A-large-practice.in'
        f = open(name, 'r')
        readline = f.readline

    t = int(readline())

    for i in range(1, t+1):
        destination, num_horses = list(map(float, readline().split(' ')))

        # Parse horse
        horse_list = []
        for h in range(int(num_horses)):
            location, speed = list(map(float, readline().split(' ')))
            horse_list.append(Horse(location, speed))

        collapse_time = 0
        output = calculate_speed(destination, horse_list, collapse_time)
        print("Case #{}: {}".format(i, output))

    if not FROM_STDIN:
        f.close()
