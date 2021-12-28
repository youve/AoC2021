#!/bin/env python3

import fileinput


def parse_input(lines):
    return [line.strip() for line in lines]


def get_corrupted_score(symbol):
    values = {}
    values[')'] = 3
    values[']'] = 57
    values['}'] = 1197
    values['>'] = 25137
    return values[symbol]


def get_incomplete_score(symbols):
    values = {}
    values['('] = 1
    values['['] = 2
    values['{'] = 3
    values['<'] = 4
    score = 0
    for symbol in symbols:
        score *= 5
        score += values[symbol]
    return score


def parse_line(line):
    # [({(<(())[]>[[{[]{<()<>>
    openings = "([{<"
    closings = ")]}>"
    stack = []

    for symbol in line:
        if symbol in openings:
            stack.append(symbol)
        else:
            if closings.index(symbol) == openings.index(stack[-1]):
                stack.pop()
            else:
                # Part 1:
                # return get_corrupted_score(symbol)
                # Part 2:
                return 0
    # Part 1:
    # return 0
    # Part 2:
    return get_incomplete_score(stack[::-1])


lines = parse_input(fileinput.input())

# Part 1
print(sum([parse_line(line) for line in lines]))

# Part 2
scores = sorted([parse_line(line) for line in lines])
scores = [score for score in scores if score > 0]
middle = len(scores)//2
print(scores[middle])
