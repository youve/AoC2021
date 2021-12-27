#!/bin/env python3

"""
.zzzz.
y....w
y....w
.xxxx.
v....t
v....t
.uuuu.

0: tuvw yz  group 6
1: t  w     group 2 *
2:  uvwx z  group 5
3: tu wx z  group 5
4: t  wxy   group 4 *
5: tu  xyz  group 5
6: tuv xyz  group 6
7: t  w  z  group 3 *
8: tuvwxyz  group 7 *
9: tu wxyz  group 6
"""

with open('input') as f:
    '''each input line looks like:
    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n'''
    inputs = [[[''.join(sorted(word))
        for word in half.split()]
            for half in line.strip().split(' | ')]
                for line in f.readlines()]

def solve_a(inputs):
    counter = 0
    for line in inputs:
        for display in line[1]:
            if len(display) in (2, 3, 4, 7):
                counter += 1
    return counter

def find_zero(line):
    six = find_six(line)
    four = find_four(line)
    for piece in line:
        if len(piece) == 6:
            if piece != six:
                for letter in four:
                    if letter not in piece:
                        return piece

def find_one(line):
    for piece in line:
        if len(piece) == 2:
            return piece

def find_two(line):
    three = find_three(line)
    six = find_six(line)
    for piece in line:
        if len(piece) == 5 and piece != three:
            differences = 0
            for letter in six:
                if letter not in piece:
                    differences += 1
            if differences == 2:
                return piece

def find_three(line):
    one = find_one(line)
    for piece in line:
        if len(piece) == 5:
            for letter in one:
                if letter not in piece:
                    break
            else:
                return piece

def find_four(line):
    for piece in line:
        if len(piece) == 4:
            return piece

def find_five(line):
    three = find_three(line)
    six = find_six(line)
    for piece in line:
        if len(piece) == 5:
            differences = 0
            for letter in six:
                if letter not in piece:
                    differences += 1
            if differences == 1:
                return piece

def find_six(line):
    one = find_one(line)
    for piece in line:
        if len(piece) == 6:
            for letter in one:
                if letter not in piece:
                    return piece

def find_seven(line):
    for piece in line:
        if len(piece) == 3:
            return piece

def find_eight(line):
    for piece in line:
        if len(piece) == 7:
            return piece

def find_nine(line):
    zero = find_zero(line)
    six = find_six(line)
    for piece in line:
        if len(piece) == 6 and piece != zero and piece != six:
            return piece

def get_four_digit_number(line):
    zero = find_zero(line[0])
    one = find_one(line[0])
    two = find_two(line[0])
    three = find_three(line[0])
    four = find_four(line[0])
    five = find_five(line[0])
    six = find_six(line[0])
    seven = find_seven(line[0])
    eight = find_eight(line[0])
    nine = find_nine(line[0])
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    answer = 1000*numbers.index(line[1][0])
    answer += 100*numbers.index(line[1][1])
    answer += 10*numbers.index(line[1][2])
    answer += numbers.index(line[1][3])
    return answer

def solve_b(lines):
    return sum([get_four_digit_number(line) for line in lines])


print(f"Part 1: {solve_a(inputs)}")
print(f"Part 2: {solve_b(inputs)}")
