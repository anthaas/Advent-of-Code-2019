#!/usr/bin/env python3

def check_adjacent_numbers(number):
	adjacent_numbers = ["11", "22", "33", "44", "55", "66", "77", "88", "99"]
	for adjacent_number in adjacent_numbers:
		if adjacent_number in str(number):
			return True
	return False


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