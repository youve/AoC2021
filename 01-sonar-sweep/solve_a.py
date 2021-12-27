#! /bin/env python3

with open("./input.txt", "r") as f:
    depths = [int(x) for x in f.readlines()]

counter = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        counter += 1
print(counter)
