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


#create set where x,y is key and 1 is the value
#create dict from wire1
#create dict from wire2
#get intersection on dicts
#calculate manhattan distance on result
#select minimum
def get_min_distance_intersection(wire1, wire2):
	path_of_wire1 = get_path_of_wire(wire1)
	path_of_wire2 = get_path_of_wire(wire2)
	intersection = set(path_of_wire1.keys()) & set(path_of_wire2.keys())
	distances = [sum(x) for x in intersection]
	return min(distances)


#wire1 = ['R8','U5','L5','D3']
#wire2 = ['U7','R6','D4','L4']

with open('input.txt') as f:
	input = f.readlines()
	wire1 = input[0].split(",")
	wire2 = input[1].split(",")
	result = get_min_distance_intersection(wire1, wire2)
	print(result)
    
