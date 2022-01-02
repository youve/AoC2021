#!/bin/env python3

import fileinput
import readline

TARGET_X_MIN = 244
TARGET_X_MAX = 303
TARGET_Y_MIN = -91
TARGET_Y_MAX = -54
START = (0, 0)


def parse_input(line):
    x_velocity, y_velocity = [int(i) for i in line.strip().split(",")]
    shoot_probe(x_velocity, y_velocity)


def move_probe(x, y, x_velocity, y_velocity):
    x += x_velocity
    y += y_velocity
    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1
    y_velocity -= 1
    return x, y, x_velocity, y_velocity


def shoot_probe(x_velocity, y_velocity):
    x, y = START
    max_seen_y = y
    while x < TARGET_X_MAX:
        x, y, x_velocity, y_velocity = move_probe(x, y, x_velocity, y_velocity)
        max_seen_y = max(y, max_seen_y)
        #print(f"At {x, y} moving {x_velocity} horizontally and {y_velocity} vertically")
        '''if x < TARGET_X_MIN:
            print("West of target")
        elif x > TARGET_X_MIN:
            print("East of target")
        else:
            print("Within x target")
        if y > TARGET_Y_MIN:
            print("North of target")
        elif y < TARGET_Y_MAX:
            print("South of target")
        else:
            print("Within y target")'''
        if TARGET_X_MIN <= x <= TARGET_X_MAX and \
                TARGET_Y_MIN <= y <= TARGET_Y_MAX:
            #print(f"SUCCESS, y got to {max_seen_y}")
            return 0
        elif x > TARGET_X_MAX:
            #print(f"Overshot: x {x} > {TARGET_X_MAX} y {y}: {TARGET_Y_MIN}..{TARGET_Y_MAX}, ")
            return 1
        elif y < TARGET_Y_MIN:
            #print(f"Undershot: x {x} < {TARGET_X_MIN}, y {y} < {TARGET_Y_MIN}")
            return -1
    # overshot
    return -1


def get_all_velocities():
    successes = []
    for x_velocity in range(21, 304):
        for y_velocity in range(-92, 91):
            shot = shoot_probe(x_velocity, y_velocity)
            if shot == 0:  # success
                successes.append((x_velocity, y_velocity))
    return successes

# Part 1: Solved interactively like that old gorillas.bas game

# while True:
#    parse_input(input())


successes = get_all_velocities()
print(len(successes))
