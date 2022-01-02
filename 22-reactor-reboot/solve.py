#!/bin/env python3

import fileinput
from dataclasses import dataclass
import itertools


@dataclass
class Instruction():
    bit: bool
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int


def execute(steps, cube):
    for step in steps:
        x_min = max(step.x_min, -50)
        x_max = min(step.x_max, 50)
        y_min = max(step.y_min, -50)
        y_max = min(step.y_max, 50)
        z_min = max(step.z_min, -50)
        z_max = min(step.z_max, 50)
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    cube[x][y][z] = step.bit

    return cube


def parse(file):
    steps = []
    #"on x=-54112..-39298,y=-85059..-49293,z=-27449..7877\n"
    for line in file:
        line = line.strip()
        bit = False
        if line.startswith('on'):
            bit = True
        x, y, z = line.split(',')
        x = x.split('=')
        x_min, x_max = x[1].split('..')
        y = y.split('=')
        y_min, y_max = y[1].split('..')
        z = z.split('=')
        z_min, z_max = z[1].split('..')
        steps.append(Instruction(bit, int(x_min), int(x_max),
                     int(y_min), int(y_max), int(z_min), int(z_max)))
    return steps


steps = parse(fileinput.input())

cube = [[[0 for x in range(101)] for y in range(101)] for z in range(101)]
cube = execute(steps, cube)

print(sum(itertools.chain.from_iterable(itertools.chain.from_iterable(cube))))
