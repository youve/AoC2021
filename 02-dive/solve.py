#!/bin/env python3

with open('input', 'r') as f:
    directions = [(y, int(z)) for y,z in [x.strip().split(' ') for x in f.readlines()]]

def solve_a(dirs):
    horizontal = 0
    vertical = 0
    for heading, amount in dirs:
        if heading == 'forward':
            horizontal += amount
        elif heading == 'down':
            vertical += amount
        elif heading == 'up':
            vertical -= amount
        else:
            print(f'wtf is {heading}, i have to go {amount}')
    print(f'horizontal: {horizontal}, vertical: {vertical}\n answer: {horizontal * vertical}')

def solve_b(dirs):
    horizontal = 0
    vertical = 0
    aim = 0
    for heading, amount in dirs:
        if heading == 'forward':
            horizontal += amount
            vertical += aim * amount
        elif heading == 'down':
            aim += amount
        elif heading == 'up':
            aim -= amount
        else:
            print(f'wtf is {heading}, i have to go {amount}')
    print(f'horizontal: {horizontal}, vertical: {vertical}\n answer: {horizontal * vertical}')

print("Part 1:")
solve_a(directions)
print("\nPart 2:")
solve_b(directions)
