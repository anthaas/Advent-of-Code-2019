#!/usr/bin/python3

dict = {}

with open('input.txt') as f:
	for line in f:
		parent,child = line.rstrip().split(")")
		dict[child] = parent


def calculate_orbit(element):
	if dict.get(element) != None:
		return 1 + calculate_orbit(dict.get(element))
	return 0


unique_objects = set(list(dict.keys()) + list(dict.values()))
result = 0
for element in unique_objects:
	result = result + calculate_orbit(element)

print(result)
