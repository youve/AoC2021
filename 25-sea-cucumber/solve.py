#!/bin/env python3

import fileinput


def parse(file):
    seabed = []
    for line in file:
        row = []
        for char in line:
            if char == '.':
                row.append(0)
            elif char == '>':
                row.append(1)
            elif char == 'v':
                row.append(2)
        seabed.append(row)
    return seabed


def tick(seabed):
    old_seabed = []
    counter = 0
    while old_seabed != seabed:
        counter += 1
        old_seabed = seabed[:]
        seabed = move_east(seabed)
        seabed = move_south(seabed)
        print(f"\nAfter {counter}:")
        show_seabed(seabed)
    return counter


def move_east(seabed):
    new_seabed = []
    for row in seabed:
        new_row = row[:]
        skip = False
        for i, char in enumerate(row):
            if skip:
                skip = False
                continue
            if char == 1 and can_move_east(row, i):
                new_row[i] = 0
                _, j = get_se_neighbour(seabed, 0, i)
                new_row[j] = 1
                skip = True
        new_seabed.append(new_row)
    return new_seabed


def move_south(seabed):
    new_seabed = seabed[:]
    for i, row in enumerate(seabed):
        new_row = row[:]
        for j, char in enumerate(new_row):
            if char == 3:
                new_row[j] = 2
                continue
            if char == 2:
                if can_move_south(seabed, [i, j]):
                    new_i, _ = get_se_neighbour(seabed, i, j)
                    if new_i == 0:
                        new_seabed[new_i][j] = 2
                    else:
                        new_seabed[new_i][j] = 3
                    new_row[j] = 0
                else:
                    new_row[j] = 2
        new_seabed[i] = new_row
    return new_seabed


def get_se_neighbour(seabed, i, j):
    i += 1
    j += 1
    if i == len(seabed):
        i = 0
    if j == len(seabed[0]):
        j = 0
    return i, j


def can_move_south(seabed, cuke):
    if cuke[0] == len(seabed) - 1:
        j = 0
    else:
        j = cuke[0] + 1
    return seabed[j][cuke[1]] == 0


def can_move_east(row, cuke):
    i = cuke + 1
    if i == len(row):
        i = 0
    return row[i] == 0


def show_seabed(seabed):
    for i, row in enumerate(seabed):
        line = []
        for j, char in enumerate(row):
            if char == 0:
                line.append('.')
            elif char == 1:
                if can_move_east(row, j):
                    line.append('\033[34;1m>\033[0m')
                else:
                    line.append('\033[31;2m>\033[0m')
            elif char == 2:
                if can_move_south(seabed, [i, j]):
                    line.append('\033[34mv\033[0m')
                else:
                    line.append('\033[31;2mv\033[0m')
            else:
                print(f"unexpected char {char}")
        print(''.join(line))


seabed = parse(fileinput.input())
show_seabed(seabed)
print(tick(seabed))
