#!/bin/env python3

with open('input', 'r') as f:
    binary = [y.strip() for y in f.readlines()]

def solve_a(binary):
    signal_length = len(binary[0])
    majority_threshhold = len(binary) // 2
    multiplier = 2**(signal_length -1)
    gamma = 0
    epsilon = 0
    for i in range(0,signal_length):
        if sum([int(x[i]) for x in binary]) > majority_threshhold:
            gamma += multiplier
        else:
            epsilon += multiplier
        multiplier >>= 1
    return gamma, epsilon

def get_most_common_bit(arr, position):
    ans = sum([int(x[position]) for x in arr])
    if ans == (len(arr) // 2):
        return 1
    else:
        return ans > (len(arr) // 2)

def solve_b(binary):
    signal_length = len(binary[0])
    oxygen_candidates = []
    co2_candidates = []
    oxygen_answer = "0"
    co2_answer = "0"
    first_common_bit = get_most_common_bit(binary, 0)
    for sign in binary: 
        if first_common_bit == 1 and int(sign[0]) == 1:
            oxygen_candidates.append(sign)
        else:
            co2_candidates.append(sign)
    for i in range(1, signal_length):
        oxy_bit = get_most_common_bit(oxygen_candidates, i)
        co2_bit = get_most_common_bit(co2_candidates, i)
        oxygen_candidates = [x for x in oxygen_candidates if int(x[i]) == oxy_bit]
        co2_candidates = [x for x in co2_candidates if int(x[i]) == co2_bit]
        if len(oxygen_candidates) == 1:
            oxygen_answer = str(oxygen_candidates[0])
        if len(co2_candidates) == 1:
            co2_answer = str(co2_candidates[0])
    return int(oxygen_answer, 2) * int(co2_answer, 2)

def get_oxygen_answer(arr):
    oxygen_candidates = arr[:]
    position = 0
    while len(oxygen_candidates) > 1:
        oxy_bit = get_most_common_bit(oxygen_candidates, position)
        oxygen_candidates = [x for x in oxygen_candidates if int(x[position]) == oxy_bit]
        position += 1
    return oxygen_candidates[0]

def get_co2_answer(arr):
    co2_candidates = arr[:]
    position = 0
    while len(co2_candidates) > 1:
        most_common = get_most_common_bit(co2_candidates, position)
        co2_candidates = [x for x in co2_candidates if int(x[position]) != most_common]
        position += 1
    return co2_candidates[0]

gamma, epsilon = solve_a(binary)
print(f"Part 1: {gamma * epsilon}")

oxy = get_oxygen_answer(binary)
co2 = get_co2_answer(binary)
print(f"Part 2: {int(oxy,2) * int(co2,2)}")
