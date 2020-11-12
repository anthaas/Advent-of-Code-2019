#!/usr/bin/python3

width = 25
height = 6

with open('input.txt') as f:
	encoded_images = f.read()
	layers = [encoded_images[i:i+(width*height)] for i in range(0,len(encoded_images),(width*height))]
	layer_analyzer = {}
	for layer in layers:
		layer_analyzer[layer.count("0")] = layer.count("1") * layer.count("2")
	
	result = layer_analyzer.get(min(layer_analyzer.keys()))
	print(result)
