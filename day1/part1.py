#!/usr/bin/env python3

import math

def calculate_mass_for_unit(mass):
    return math.trunc(mass/3) - 2

f = open('input.txt', 'r')
input = [int(line) for line in f]
f.close()

result = sum(map(calculate_mass_for_unit, input))
print(result)

