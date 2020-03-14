#!/usr/bin/env python3

import math

def calculate_mass_for_unit(mass):
    fuel = math.trunc(mass/3) - 2
    return fuel if (fuel <= 0) else fuel + calculate_mass_for_unit(fuel)


f = open('input.txt', 'r')
input = [int(line) for line in f]
f.close()

result = sum(map(calculate_mass_for_unit, input))
print(result)

