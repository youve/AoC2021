#!/bin/env python3

import fileinput


def parse_file(file):
    for line in file:
        hex_data = line.strip()
    bin_data = bin(int(hex_data, 16))[2:].zfill(4 * len(hex_data))
    return bin_data


def get_version(bits):
    return 3, int(bits[0:3], 2)


def get_type(bits):
    return get_version(bits)


def get_literal(bits):
    print(bits)
    value = []
    i = 0
    read_more = '0'
    while read_more == '1' or i == 0:
        read_more = bits[i]
        i += 1
        print(f"Read more: {read_more}")
        value.append(bits[i:i+4])
        print(value[-1])
        i += 4
    literal = int(''.join(value), 2)
    print(f"get_literal returning {i, literal}")
    return i, literal


def get_operator(bits):
    values = []
    packet_version = 0
    length_type_id = bits[0]
    packet_value = 0
    cut = 1
    if length_type_id == '0':
        total_length = int(bits[cut:16], 2)
        cut = 16
        new_cut = 0
        while cut < total_length:
            new_cut, new_version = process_packet(bits[cut:cut+total_length])
            print(f"Got a version {new_version}")
            packet_version += new_version
            cut += new_cut
            print(cut, total_length)
        print("Done subpackets")
    elif length_type_id == '1':
        number_of_subpackets = int(bits[cut:12], 2)
        print(f"There are {number_of_subpackets} subpackets")
        cut += 11
        for _ in range(number_of_subpackets):
            new_cut, new_version = process_packet(bits[cut:])
            print(f"Got a new version {new_version}")
            packet_version += new_version
            cut += new_cut
    print(f"get_operator returning {cut, packet_version}")
    return cut, packet_version


def process_packet(bits):
    cut, packet_version = get_version(bits)
    new_cut, packet_type = get_type(bits[cut:])
    cut += new_cut
    print(
        f"This is a packet version {packet_version} of type {packet_type} containing the bits \n{bits[cut:]}")
    if packet_type == 4:  # literal value
        new_cut, packet_value = get_literal(bits[cut:])
        print(f"The packet's value was {packet_value}")
    else:
        new_cut, new_version = get_operator(bits[cut:])
        packet_version += new_version
    cut += new_cut
    print(f"process packet returning {cut, packet_version}")
    return cut, packet_version


bin_data = parse_file(fileinput.input())

version_sum = 0
cut = 0
while len(bin_data) > 0 and int(bin_data) != 0:
    cut, new_version = process_packet(bin_data)
    version_sum += new_version
    bin_data = bin_data[cut:]
    print(version_sum, bin_data)

print(version_sum)
