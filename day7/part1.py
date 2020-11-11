#!/usr/bin/python3
import itertools

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

def run(memory, phase, input):
	init = True
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
			memory[memory[index+1]] = phase if init else input
			init = False
			index = index + 2
		# output
		elif opcode == 4:			
			return memory[index+1] if param1_mode == 1 else memory[memory[index+1]]
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


def find_max_thruster_signal(data):
	thruster_signals = []
	for permutation in list(itertools.permutations([0,1,2,3,4])):
		a,b,c,d,e = permutation
		amp_a = run(data, a, 0)
		amp_b = run(data, b, amp_a)
		amp_c = run(data, c, amp_b)
		amp_d = run(data, d, amp_c)
		amp_e = run(data, e, amp_d)
		thruster_signals.append(amp_e)
	return max(thruster_signals)

with open('input.txt') as f:
	data = [int(value) for value in f.readline().split(",")]
	print(find_max_thruster_signal(data))


