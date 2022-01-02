#!/bin/env python3

import fileinput
import sys
import itertools


def parse_file(file):
    # "[[2,[[1,1],9]],[[0,[3,0]],[[1,6],[4,2]]]]\n"
    problems = []
    for line in file:
        problems.append(line.strip())
    return problems


def add(first, second):
    answer = ""
    new_answer = "[" + first + "," + second + "]"
    counter = 0
    while (answer != new_answer):
        counter += 1
        answer = new_answer
        new_answer = explode(answer)  # perform all explosions
        new_answer = split(new_answer)  # perform one split
    return answer


def explode(answer):
    depth = depth = find_out_of_depth(answer)
    while depth != -1:
        i = 1
        exploding_left = ""
        while answer[depth + i].isdigit():
            exploding_left += answer[depth + i]
            i += 1
        i += 1
        exploding_right = ""
        while answer[depth + i].isdigit():
            exploding_right += answer[depth + i]
            i += 1
        left_node = ""
        j = -1
        while not answer[depth + j].isdigit() and depth + j > 0:
            j -= 1
        while answer[depth + j].isdigit() and depth + j > 0:
            left_node = answer[depth + j] + left_node
            j -= 1
        left_node_index = depth + j
        i += 1
        right_node = ""
        while not answer[depth + i].isdigit() and depth + i + 1 < len(answer):
            i += 1
        right_node_index = depth + i
        while answer[depth + i].isdigit() and depth + i < len(answer):
            right_node = right_node + answer[depth + i]
            i += 1
        if left_node:
            new_left_node = int(left_node) + int(exploding_left)
        if right_node:
            new_right_node = int(right_node) + int(exploding_right)
        if right_node and not left_node:
            middle_index = depth + 3 + \
                len(exploding_left) + len(exploding_right)
            answer = answer[:depth] + '0' + answer[middle_index:right_node_index] + \
                str(new_right_node) + \
                answer[right_node_index + len(right_node):]
        elif left_node and not right_node:
            right_node_index = depth + \
                len(exploding_left) + len(exploding_right) + 3
            answer = answer[:left_node_index + len(left_node)] + str(
                new_left_node) + ',0' + answer[right_node_index:]
        else:
            r_middle_index = depth + \
                len(exploding_left) + len(exploding_right) + 3
            l_middle_index = left_node_index + len(left_node) + 1
            tail = right_node_index + len(right_node)
            answer = answer[:left_node_index + 1] + str(new_left_node) + answer[l_middle_index:depth] + \
                '0' + answer[r_middle_index:right_node_index] + \
                str(new_right_node) + answer[tail:]
        depth = find_out_of_depth(answer)

    return answer


def find_out_of_depth(answer):
    braces = []
    for i, v in enumerate(answer):
        if v == "[":
            braces.append(v)
            # make sure this is a [n,n] not a [n,[
            if len(braces) > 4:
                j = i + 1
                while answer[j].isdigit():
                    j += 1
                j += 1
                if answer[j].isdigit():
                    return i
                else:
                    print(answer[i:])
                    continue
        elif v == "]":
            braces.pop()
    return -1


def split(answer):
    i, digits = find_two_digits(answer)
    if i == -1:
        return answer
    number = int(digits)
    if number % 2 == 0:
        new_number = f"[{number // 2},{number // 2}]"
    else:
        new_number = f"[{number // 2},{number // 2 + 1}]"
    j = i + len(digits)
    return answer[:i] + new_number + answer[j:]


def find_two_digits(answer):
    digits = []
    for i, v in enumerate(answer):
        if not v.isdigit():
            if len(digits) > 1:
                return i - len(digits), ''.join(digits)
            else:
                digits = []
        else:
            digits.append(v)
    return -1, ''


def get_magnitude(answer):
    """checks the magnitude of the final sum. The magnitude of a pair is 
    3 times the magnitude of its left element plus 
    2 times the magnitude of its right element. 
    The magnitude of a regular number is just that number."""
    left = 0
    right = 0
    if isinstance(answer[0], int):
        left = 3 * answer[0]
    else:
        left = 3 * get_magnitude(answer[0])
    if isinstance(answer[1], int):
        right = 2 * answer[1]
    else:
        right = 2 * get_magnitude(answer[1])
    return left + right


def solve_part_1():
    problems = parse_file(fileinput.input())
    answer = problems[0]
    for i, problem in enumerate(problems[1:]):
        answer = add(answer, problem)
    answer = eval(answer)
    print(f"Part 1: {get_magnitude(answer)}")


def solve_part_2():
    maximum = 0
    problems = parse_file(fileinput.input())
    for pair in itertools.permutations(problems, 2):
        answer = add(*pair)
        maximum = max(maximum, get_magnitude(eval(answer)))
    print(f"Part 2: {maximum}")


solve_part_1()
solve_part_2()
