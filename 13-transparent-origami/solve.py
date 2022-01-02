#!/bin/env python3

import fileinput


def parse_input(lines):
    input_dict = {}
    input_dict['folds'] = []
    input_dict['coords'] = []
    for line in lines:
        line = line.strip()
        if line.startswith('f'):
            fold = line.split(" ")[-1]
            val = int(fold.split("=")[-1])
            if fold.startswith("x"):
                input_dict['folds'].append(("x", val))
            else:
                input_dict['folds'].append(("y", val))
        elif len(line):
            x, y = line.split(",")
            input_dict['coords'].append((int(x), int(y)))
    return input_dict


def fold_up(transparency, y_fold):
    new_coords = []
    for x, y in transparency['coords']:
        if y > y_fold:
            difference = y - y_fold
            y = y_fold - difference
        new_coords.append((x, y))
    transparency['coords'] = new_coords
    return transparency


def fold_left(transparency, x_fold):
    new_coords = []
    for x, y in transparency['coords']:
        if x > x_fold:
            difference = x - x_fold
            x = x_fold - difference
        new_coords.append((x, y))
    transparency['coords'] = new_coords
    return transparency


def fold_transparency(transparency):
    for fold in transparency['folds']:
        if fold[0] == 'x':
            print('Folding left:')
            transparency = fold_left(transparency, fold[1])
            display_transparency(transparency)
        else:
            print('Folding up:')
            transparency = fold_up(transparency, fold[1])
            display_transparency(transparency)
    return transparency


def display_transparency(transparency):
    coords = set(transparency['coords'])
    max_x = max(coord[0] for coord in coords) + 1
    max_y = max(coord[1] for coord in coords) + 1
    picture = [[0 for x in range(max_x)] for y in range(max_y)]
    for x, y in coords:
        picture[y][x] = 8
    for line in picture:
        print("".join(['░' if x == 0 else '▓' for x in line]))
    print()


transparency = parse_input(fileinput.input())
transparency = fold_transparency(transparency)
