#!/bin/env python3
import numpy as np

def parse(data):
    vents = []
    for line in data:
        vents.append([int(s) for s in line.replace(" -> ",",").strip().split(",") if s.isdigit()])
    return vents

def map_seabed(seabed, data):
    for line in data:
        x1, y1, x2, y2 = line
        if x1 == x2:
            y1, y2 = min([y1, y2]), max([y1, y2])
            for y in range(y1, y2 + 1):
                seabed[y,x1] += 1
        elif y1 == y2:
            x1, x2 = min([x1, x2]), max([x1, x2])
            for x in range(x1, x2 + 1):
                seabed[y1,x] += 1
        elif x1 < x2:
            while x1 <= x2:
                seabed[y1,x1] += 1
                x1 +=1
                if y1 < y2:
                    y1 += 1
                else:
                    y1 -= 1
        elif x2 < x1:
            while x2 <= x1:
                seabed[y2,x2] += 1
                x2 +=1
                if y1 < y2:
                    y2 -= 1
                else:
                    y2 += 1
        else:
            print("now what")
    return seabed

def find_danger(seabed):
    return np.sum(np.where(seabed > 1, 1, 0))

def test():
    with open('test_input', 'r') as f:
        data = f.readlines()
    vents=parse(data)
    seabed = np.zeros((10,10), dtype=int)
    seabed = map_seabed(seabed, vents)
    print(seabed)
    print(find_danger(seabed))

def solve():
    with open('input', 'r') as f:
        data = f.readlines()
    vents=parse(data)
    seabed = np.zeros((1000,1000), dtype=int)
    seabed = map_seabed(seabed, vents)
    print(find_danger(seabed))

solve()
