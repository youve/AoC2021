#!/bin/env python3

import fileinput
import numpy as np


def parse_input(lines, part2=False):
    two_d_int_arr = [[int(digit)
                      for digit in line.strip()]
                     for line in lines]
    if part2:
        two_d_int_arr = make_bigger_cave(two_d_int_arr)
    return np.array(two_d_int_arr)


def get_neighbour_indices(x, y, arr, diagonal=False):
    max_x, max_y = arr_size(arr)
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < max_x:
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < max_y:
        neighbours.append((x, y + 1))
    if x > 0 and y > 0 and diagonal:
        neighbours.append((x - 1, y - 1))
    if x < max_x and y < max_y and diagonal:
        neighbours.append((x + 1, y + 1))
    if x > 0 and y < max_y and diagonal:
        neighbours.append((x - 1, y + 1))
    if y > 0 and x < max_x and diagonal:
        neighbours.append((x + 1, y - 1))
    return neighbours


def arr_size(two_d_arr):
    max_y = len(two_d_arr[0]) - 1
    max_x = len(two_d_arr) - 1
    return max_x, max_y


def dijkstra(cave):
    max_x, max_y = arr_size(cave)
    visited = np.zeros((max_y + 1, max_x + 1), bool)
    max_dist = 10 * (1 + max_x) * (1 + max_y)
    distances = np.full((max_y + 1, max_x + 1), max_dist, int)
    current = (0, 0)
    distances[0][0] = 0
    goal = (max_y, max_x)
    frontier = {current}
    while current != goal:
        curr_y, curr_x = current
        current_neighbours = get_neighbour_indices(*current[::-1], cave)
        for x, y in current_neighbours:
            if not visited[y][x]:
                distances[y][x] = min(
                    distances[y][x], distances[curr_y][curr_x] + cave[y][x])
                frontier.add((y, x))
        visited[curr_y][curr_x] = True
        frontier.remove((curr_y, curr_x))
        current = min(
            frontier, key=lambda coords: distances[coords[0]][coords[1]])
    return distances[goal[0]][goal[1]]


def make_bigger_cave(cave):
    new_cave = []
    for row in cave:
        new_row = row + [x + 1 for x in row] + [x + 2 for x in row] + \
            [x + 3 for x in row] + [x + 4 for x in row]
        new_row = [x if x < 10 else x - 9 for x in new_row]
        new_cave.append(new_row)
    new_new_cave = []
    for n in range(5):
        for row in new_cave:
            new_row = [x + n for x in row]
            new_row = [x if x < 10 else x - 9 for x in new_row]
            new_new_cave.append(new_row)
    return new_new_cave


def print_arr(arr):
    for row in arr:
        print(''.join(str(x) for x in row))


# Part 1
# caves = parse_input(fileinput.input())
# Part 2
caves = parse_input(fileinput.input(), part2=True)
print(dijkstra(caves))
