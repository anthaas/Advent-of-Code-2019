#!/usr/bin/env python3

def is_bigger_group(founded_adjacent, number):
	return str(founded_adjacent)+str(founded_adjacent)[0] in str(number)


def check_adjacent_numbers(number):
	adjacent_numbers = ["11", "22", "33", "44", "55", "66", "77", "88", "99"]
	founded_adjacents = []
	for adjacent_number in adjacent_numbers:
		if adjacent_number in str(number):
			founded_adjacents.append(adjacent_number)
	all_adjacents_part_of_bigger_group = map(is_bigger_group, founded_adjacents, [number] * len(founded_adjacents))
	return False in all_adjacents_part_of_bigger_group


def check_never_decrease_criteria(number):
	for i in range(len(str(number))-1):
		if int(str(number)[i]) > int(str(number)[i+1]):
			return False
	return True


def check_combinations(low_range, high_range):
	correct_combinations = 0
	for i in range(low_range, high_range):
		if (check_adjacent_numbers(i) and check_never_decrease_criteria(i)):
			correct_combinations = correct_combinations+1
		
	return correct_combinations


low_range = 387638
high_range = 919123
result = check_combinations(low_range, high_range)
print(result)