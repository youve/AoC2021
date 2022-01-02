#!/bin/env python3

import fileinput
import collections


def parse_input(lines):
    polymer = {}
    polymer['rules'] = {}
    for line in lines:
        line = line.strip()
        if "->" in line:
            polymer['rules'][line[0:2]] = line[-1]
        elif line:
            polymer['template'] = [x for x in line]
    return polymer


def perform_insertions(polymer):
    # Part 1
    insertion_queue = []
    counter = 0
    for i in range(1, len(polymer['template'])):
        pair = ''.join(polymer['template'][i-1:i+1])
        if pair in polymer['rules'].keys():
            insertion_queue.append((i + counter, polymer['rules'][pair]))
            counter += 1
    for i, val in insertion_queue:
        polymer['template'].insert(i, val)
    return polymer


def prepare_template(polymer):
    template = {}
    for i in range(1, len(polymer['template'])):
        pair = ''.join(polymer['template'][i-1:i+1])
        if pair in template:
            template[pair] += 1
        else:
            template[pair] = 1
    polymer['template'] = template
    return polymer


def pretend_to_perform_insertions(polymer):
    # Part 2
    changes = {}
    for rule in polymer['rules'].keys():
        if rule in polymer['template'].keys() and polymer['template'][rule] > 0:
            times = polymer['template'][rule]
            if rule in changes:
                changes[rule] -= times
            else:
                changes[rule] = -times
            new_a = rule[0] + polymer['rules'][rule]
            new_b = polymer['rules'][rule] + rule[1]
            for pair in [new_a, new_b]:
                if pair in changes:
                    changes[pair] += times
                else:
                    changes[pair] = times
    for change in changes.keys():
        if change in polymer['template'].keys():
            polymer['template'][change] += changes[change]
        else:
            polymer['template'][change] = changes[change]
    return polymer


def get_answer(polymer):
    poly_count = collections.Counter(polymer['template'])
    print(poly_count)
    return poly_count.most_common()[0][-1] - poly_count.most_common()[-1][-1]


def get_letter_counts(polymer, first_letter):
    letter_sums = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        total = sum(polymer['template'][key]
                    for key in polymer['template'].keys() if letter in key[1])
        if total:
            letter_sums[letter] = total
    letter_sums[first_letter] += 1
    return letter_sums


polymer = parse_input(fileinput.input())
first_letter = polymer['template'][0]
polymer = prepare_template(polymer)

for _ in range(40):
    polymer = pretend_to_perform_insertions(polymer)

letters = get_letter_counts(polymer, first_letter)
print(f"Part 2: {max(letters.values()) - min(letters.values())}")
