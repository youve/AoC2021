#!/bin/env python3

import fileinput
import collections


def parse_input(lines):
    caves = {}
    for line in lines:
        cave_a, cave_b = line.strip().split('-')
        if cave_a in caves:
            caves[cave_a].append(cave_b)
        else:
            caves[cave_a] = [cave_b]
        if cave_b in caves:
            caves[cave_b].append(cave_a)
        else:
            caves[cave_b] = [cave_a]
    return caves


def find_paths(caves):  # part 1
    stack = [['start']]
    paths = []
    counter = 0
    while len(stack) > 0:
        current_path = stack.pop()
        current_node = current_path[-1]
        for val in caves[current_node]:
            if val == 'end' and current_path + [val] not in paths:
                paths.append(current_path + [val])
                # Uncomment to see new path
                # print(",".join(paths[-1]))
            elif val.isupper() or val not in current_path:
                stack.append(current_path + [val])
    return paths


def visited_a_small_cave_twice_already(path):
    counter = collections.Counter([x for x in path if x.islower()])
    if counter.most_common(1)[0][-1] > 1:
        return True
    return False


def find_paths_2(caves):  # part 2
    stack = [['start']]
    paths = []
    counter = 0
    while len(stack) > 0:
        current_path = stack.pop()
        current_node = current_path[-1]
        for val in caves[current_node]:
            if val == 'start':
                continue
            elif val == 'end' and current_path + [val] not in paths:
                paths.append(current_path + [val])
            elif val.isupper() or val not in current_path or not visited_a_small_cave_twice_already(current_path):
                stack.append(current_path + [val])
    return paths


def in_path(val, path):
    i = bisect.bisect_left(path, val)
    if i == len(path):
        return False
    if path[i] == val:
        return True
    return False


def find_paths_better(caves):  # part 2
    stack = [['start']]
    paths = []
    counter = 0
    while len(stack) > 0:
        current_path = stack.pop()
        current_node = current_path[-1]
        for val in caves[current_node]:
            if val == 'start':
                continue
            elif val == 'end':
                paths.append(current_path + [val])
            elif val.isupper() or val not in current_path or not visited_a_small_cave_twice_already(current_path):
                stack.append(current_path + [val])
    return paths


caves = parse_input(fileinput.input())
print(f"Part 1: {len(find_paths(caves))}")
print(f"Part 2: {len(find_paths_better(caves))}")
