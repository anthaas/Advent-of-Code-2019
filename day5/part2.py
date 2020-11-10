#!/usr/bin/python3

def process_instruction(instruction):
	instruction_length = len(instruction)
	#add leading zeros
	if instruction_length != 5:
		instruction = "0" * (5-instruction_length) + instruction
	opcode = int(instruction[3]+instruction[4])
	param1_mode = int(instruction[2])
	param2_mode = int(instruction[1])
	param3_mode = int(instruction[0])
	return opcode, param1_mode, param2_mode, param3_mode

def read_arguments(memory, index, param1_mode, param2_mode):
	value1 = memory[index+1] if param1_mode == 1 else memory[memory[index+1]]
	value2 = memory[index+2] if param2_mode == 1 else memory[memory[index+2]]
	return value1, value2

def run(memory):
	index = 0 
	opcode, param1_mode, param2_mode, param3_mode = process_instruction(str(memory[index]))

	while opcode != 99:
		# addition
		if opcode == 1:
			value1, value2 = read_arguments(memory, index, param1_mode, param2_mode)
			memory[memory[index+3]] = value1 + value2
			index = index + 4
		# multiplication
		elif opcode == 2: 
			value1, value2 = read_arguments(memory, index, param1_mode, param2_mode)
			memory[memory[index+3]] = value1 * value2
			index = index + 4
		# input
		elif opcode == 3:
			memory[memory[index+1]] = int(input("Input: "))
			index = index + 2
		# output
		elif opcode == 4:			
			print(f'Output: {memory[index+1] if param1_mode == 1 else memory[memory[index+1]]}')
			index = index + 2
		# jump if true
		elif opcode == 5:
			value1, value2 = read_arguments(memory, index, param1_mode, param2_mode)
			if value1 != 0:
				index = value2
			else:
				index = index + 3
		# jump if false
		elif opcode == 6:
			value1, value2 = read_arguments(memory, index, param1_mode, param2_mode)
			if value1 == 0:
				index = value2
			else:
				index = index + 3
		# less than
		elif opcode == 7:
			value1, value2 = read_arguments(memory, index, param1_mode, param2_mode)
			memory[memory[index+3]] = 1 if value1 < value2 else 0
			index = index + 4
		# equals
		elif opcode == 8:
			value1, value2 = read_arguments(memory, index, param1_mode, param2_mode)
			memory[memory[index+3]] = 1 if value1 == value2 else 0
			index = index + 4
		# unknown operation
		else:
			print(f'unknown opcode {opcode}')
			return
		# process next iteration
		opcode, param1_mode, param2_mode, param3_mode = process_instruction(str(memory[index]))


with open('input.txt') as f:
	data = [int(value) for value in f.readline().split(",")]
	run(data)
