#!/usr/bin/python3

dict = {}

with open('input.txt') as f:
	for line in f:
		parent,child = line.rstrip().split(")")
		dict[child] = parent


def get_path_to_root(element):
	if dict.get(element) != None:
		return [element] + get_path_to_root(dict.get(element))
	return []

path_to_root_of_you = get_path_to_root(dict.get("YOU"))
path_to_root_of_san = get_path_to_root(dict.get("SAN"))
path_you_to_san = set(path_to_root_of_you) ^ set(path_to_root_of_san)
print(len(path_you_to_san))