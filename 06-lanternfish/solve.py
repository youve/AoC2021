#!/bin/env python

def open_and_parse(file):
    '''given a file path, return a list of ints '''
    with open(file) as f:
        fish = [int(x) for x in f.readline().strip().split(',')]
    return fish

def solve_a(fish, days):
    ''' given a list of ints and an amount of days, return how many fish '''
    for _ in range(days):
        fish = [x - 1 for x in fish]
        new_fish = fish.count(-1)
        fish = fish + [8] * new_fish
        fish = [6 if b == -1 else b for b in fish]
    return len(fish)

def parse_better(file):
    fish = open_and_parse(file)
    fish_dict = {}
    for i in range(-1,10):
        fish_dict[i] = fish.count(i)
    return fish_dict

def solve_b(fish, days):
    ''' given a dict of how many fish with a given timer there are, return how many fish after days'''
    for _ in range(days):
        for i in range(0, 10): # decrement timers
            fish[i - 1] = fish[i]
        new_fish = fish[-1]
        fish[8] += new_fish
        fish[6] += new_fish
        fish[-1] = 0
    return sum(fish.values())

fish = open_and_parse('input') # list of ints
print(f"\nPart 1: {solve_a(fish,80)}")

fish = parse_better('input')

print(f"\nPart 2: {solve_b(fish, 256)}")
