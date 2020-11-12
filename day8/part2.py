#!/usr/bin/python3

width = 25
height = 6

def stack_two_layers(layer1, layer2):
	result = ""
	for pixel1,pixel2 in zip(layer1,layer2):
		result += pixel2 if pixel1 == "2" else pixel1
	return result

def print_image(image, width):
	processed_image = image.replace("0", " ").replace("1", "*")
	for i in range(0, len(processed_image), width):
		print(processed_image[i:i+width])

with open('input.txt') as f:
	encoded_images = f.read()
	layers = [encoded_images[i:i+(width*height)] for i in range(0,len(encoded_images),(width*height))]
	image = "2" * (width * height)
	for layer in layers:
		image = stack_two_layers(image, layer)

	print_image(image, width)
