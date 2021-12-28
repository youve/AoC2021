#!/bin/env python3

import fileinput
import numpy as np


def parse_input(lines):
    two_d_int_arr = [[int(digit)
                      for digit in line.strip()]
                     for line in lines]
    return np.array(two_d_int_arr)


def get_neighbour_indices(x, y, arr):
    max_y = len(arr[0]) - 1
    max_x = len(arr) - 1
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < max_x:
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < max_y:
        neighbours.append((x, y + 1))
    if x > 0 and y > 0:
        neighbours.append((x - 1, y - 1))
    if x < max_x and y < max_y:
        neighbours.append((x + 1, y + 1))
    if x > 0 and y < max_y:
        neighbours.append((x - 1, y + 1))
    if y > 0 and x < max_x:
        neighbours.append((x + 1, y - 1))
    return neighbours


def step(octopuses):
    global FLASHES

    octopuses = [[octopus + 1 for octopus in row]
                 for row in octopuses]

    affected = np.zeros((10, 10), int)
    neighbours = []
    for i, row in enumerate(octopuses):
        for j, octopus in enumerate(row):
            if octopus > 9:
                affected[i][j] = 1
                neighbours += get_neighbour_indices(i, j, octopuses)

    while len(neighbours) > 0:
        x, y = neighbours.pop()
        octopuses[x][y] += 1
        if octopuses[x][y] > 9 and not affected[x][y]:
            affected[x][y] = 1
            neighbours += get_neighbour_indices(x, y, octopuses)
            # Uncomment this to see pretty chain reactions:
            # print_octopus(octopuses)
    FLASHES += np.sum(affected)
    octopuses = [[octopus if octopus < 10 else 0 for octopus in row]
                 for row in octopuses]
    return octopuses


def print_octopus(octopuses):
    for row in octopuses:
        print(''.join(str(x) if 1 < x < 10
              else '\033[7m0\033[0m' for x in row))
    print()


def part_1(octopuses):
    global FLASHES
    print("Starting part 1")
    for i in range(100):
        print(f"Step {i}")
        print_octopus(octopuses)
        octopuses = step(octopuses)
    print(f"Step {i+1}")
    print_octopus(octopuses)
    print(f"Part 1: {FLASHES} flashes in {i+1} steps.")


def part_2(octopuses):
    global FLASHES
    print("Starting part 2")
    counter = 0
    while FLASHES != 100:
        FLASHES = 0
        print(f"Step {counter}")
        print_octopus(octopuses)
        octopuses = step(octopuses)
        counter += 1
    print(f"Part 2: Octopuses sync up after {counter} steps.")
    print_octopus(octopuses)


octopuses = parse_input(fileinput.input())
FLASHES = 0

part_1(octopuses)
part_2(octopuses)
