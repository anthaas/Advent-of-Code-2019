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

def run(memory):
	index = 0 
	opcode, param1_mode, param2_mode, param3_mode = process_instruction(str(memory[index]))

	while opcode != 99:
		if opcode == 3:
			memory[memory[index+1]] = int(input("Input: "))
			steps = 2
		elif opcode == 4:			
			print(f'Output: {memory[memory[index+1]]}')
			steps = 2
		else: 
			position1 = memory[index+1]
			position2 = memory[index+2]
			value1 = memory[index+1] if param1_mode == 1 else memory[position1]
			value2 = memory[index+2] if param2_mode == 1 else memory[position2]
			write_index = memory[index+3]
			steps = 4
			if opcode == 1:
				memory[write_index] = value1 + value2
			elif opcode == 2: 
				memory[write_index] = value1 * value2
			else:
				print(f'unknown opcode {opcode}')
				return

		index += steps
		opcode, param1_mode, param2_mode, param3_mode = process_instruction(str(memory[index]))


with open('input.txt') as f:
	data = [int(value) for value in f.readline().split(",")]
	run(data)
