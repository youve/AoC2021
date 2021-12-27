#! /bin/env python3

with open("./input.txt", "r") as f:
    depths = [int(x) for x in f.readlines()]

counter = 0
for i in range(4, len(depths) + 1):
    if sum(depths[i-4:i-1]) < sum(depths[i-3:i]):
        counter += 1
print(counter)
