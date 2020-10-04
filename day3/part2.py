#!/usr/bin/env python3

def get_path_of_wire(wire):
	path = {}
	x = 0
	y = 0
	for coord in wire:
		direction = coord[0]
		steps = int(coord[1:])
	#up and right is +, down and left is -
		if 'U' == direction:
			for i in range(steps):
				y = y+1
				path.update({(x,y):1})
		elif 'R' == direction:
			for i in range(steps):
				x = x+1
				path.update({(x,y):1})
		elif 'D' == direction:
			for i in range(steps):
				y = y-1
				path.update({(x,y):1})
		elif 'L' == direction:
			for i in range(steps):
				x = x-1
				path.update({(x,y):1})
		else:
			print("unknown operation ", operation)
			exit()	

	return path


def get_number_of_steps_to_intersection(intersection, wire1, wire2):
	steps_for_wire1 = get_number_of_steps_to_intersection_for_wire(intersection, wire1)
	steps_for_wire2 = get_number_of_steps_to_intersection_for_wire(intersection, wire2)
	return steps_for_wire1 + steps_for_wire2
	

def get_number_of_steps_to_intersection_for_wire(intersection, wire):
	intersection_x, intersection_y = intersection
	x = 0
	y = 0
	steps_from_start = 0
	for coord in wire:
		direction = coord[0]
		steps = int(coord[1:])
	#up and right is +, down and left is -
		if 'U' == direction:
			for i in range(steps):
				y = y+1
				steps_from_start = steps_from_start+1
				if intersection_x == x and intersection_y == y:
					return steps_from_start
		elif 'R' == direction:
			for i in range(steps):
				x = x+1
				steps_from_start = steps_from_start+1
				if intersection_x == x and intersection_y == y:
					return steps_from_start
		elif 'D' == direction:
			for i in range(steps):
				y = y-1
				steps_from_start = steps_from_start+1
				if intersection_x == x and intersection_y == y:
					return steps_from_start
		elif 'L' == direction:
			for i in range(steps):
				x = x-1
				steps_from_start = steps_from_start+1
				if intersection_x == x and intersection_y == y:
					return steps_from_start
		else:
			print("unknown operation ", operation)
			exit()	

	return steps_from_start


#create set where x,y is key and 1 is the value
#create dict from wire1
#create dict from wire2
#get intersection on dicts
#for every intersection calculate number of steps fo both wires to reach it
#select minimum
def get_min_distance_intersection(wire1, wire2):
	path_of_wire1 = get_path_of_wire(wire1)
	path_of_wire2 = get_path_of_wire(wire2)
	intersections = set(path_of_wire1.keys()) & set(path_of_wire2.keys())
	steps_to_intersection = [get_number_of_steps_to_intersection(x, wire1, wire2) for x in intersections]
	return min(steps_to_intersection)


#tests
#case1
wire1 = ['R8','U5','L5','D3']
wire2 = ['U7','R6','D4','L4']
expected_value = 30
result = get_min_distance_intersection(wire1, wire2)
assert result == expected_value


#case2
wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
expected_value = 610
result = get_min_distance_intersection(wire1, wire2)
assert result == expected_value


#case3
wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
expected_value = 410
result = get_min_distance_intersection(wire1, wire2)
assert result == expected_value


with open('input.txt') as f:
	input = f.readlines()
	wire1 = input[0].split(",")
	wire2 = input[1].split(",")
	result = get_min_distance_intersection(wire1, wire2)
	print(result)

                
