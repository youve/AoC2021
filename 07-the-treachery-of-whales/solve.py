#!/bin/env python
import math

with open('input') as f:
    h_positions = sorted([int(x) for x in f.readline().strip().split(',')])

def find_peak(arr):
    original_guess = round(sum(arr)/len(arr))
    guess = original_guess
    lowest = min(arr)
    highest = max(arr)
    guess_lower = max(lowest, guess - 1)
    guess_higher = min(highest, guess + 1)
    while fuel(arr, guess) > fuel(arr, guess_higher) and guess_higher <= highest:
        guess += 1
        guess_higher += 1
    fuel_guess_a = fuel(arr, guess)
    guess = original_guess
    while (fuel(arr, guess) > fuel(arr, guess_lower)) and guess_lower >= lowest:
        guess -= 1
        guess_lower -= 1
    fuel_guess_b = fuel(arr, guess)
    return min(fuel_guess_a, fuel_guess_b)

def fuel_a(arr, mean):
    return sum([abs(x - mean) for x in arr])

def fuel(arr, mean):
    return sum([nth_triangle(abs(x - mean)) for x in arr])

def nth_triangle(n):
    return sum(range(1,n+1))

print(find_peak(h_positions))
#print(fuel(h_positions, 479))
