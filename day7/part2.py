#!/usr/bin/python3
import itertools

class Amp:
	def __init__(self,memory,phase):
		self.memory = memory
		self.phase = phase
		self.first_run = True
		self.index = 0

	def run(self, input):
		opcode, param1_mode, param2_mode, param3_mode = self.process_instruction()

		while opcode != 99:
			# addition
			if opcode == 1:
				value1, value2 = self.read_arguments(param1_mode, param2_mode)
				self.memory[self.memory[self.index+3]] = value1 + value2
				self.index += 4
			# multiplication
			elif opcode == 2: 
				value1, value2 = self.read_arguments(param1_mode, param2_mode)
				self.memory[self.memory[self.index+3]] = value1 * value2
				self.index += 4
			# input
			elif opcode == 3:
				self.memory[self.memory[self.index+1]] = self.phase if self.first_run else input
				self.first_run = False
				self.index += 2
			# output
			elif opcode == 4:
				result = self.memory[self.index+1] if param1_mode == 1 else self.memory[self.memory[self.index+1]]	
				self.index += 2		
				return result
			# jump if true
			elif opcode == 5:
				value1, value2 = self.read_arguments(param1_mode, param2_mode)
				if value1 != 0:
					self.index = value2
				else:
					self.index += 3
			# jump if false
			elif opcode == 6:
				value1, value2 = self.read_arguments(param1_mode, param2_mode)
				if value1 == 0:
					self.index = value2
				else:
					self.index += 3
			# less than
			elif opcode == 7:
				value1, value2 = self.read_arguments(param1_mode, param2_mode)
				self.memory[self.memory[self.index+3]] = 1 if value1 < value2 else 0
				self.index += 4
			# equals
			elif opcode == 8:
				value1, value2 = self.read_arguments(param1_mode, param2_mode)
				self.memory[self.memory[self.index+3]] = 1 if value1 == value2 else 0
				self.index += 4
			# unknown operation
			else:
				print(f'unknown opcode {opcode}')
				exit("unknown opocode")
			# process next iteration
			opcode, param1_mode, param2_mode, param3_mode = self.process_instruction()
	
		return "Halted"

	def process_instruction(self):
		instruction = str(self.memory[self.index])
		instruction_length = len(instruction)
		#add leading zeros
		if instruction_length != 5:
			instruction = "0" * (5-instruction_length) + instruction
		opcode = int(instruction[3]+instruction[4])
		param1_mode = int(instruction[2])
		param2_mode = int(instruction[1])
		param3_mode = int(instruction[0])
		return opcode, param1_mode, param2_mode, param3_mode

	def read_arguments(self,param1_mode, param2_mode):
		value1 = self.memory[self.index+1] if param1_mode == 1 else self.memory[self.memory[self.index+1]]
		value2 = self.memory[self.index+2] if param2_mode == 1 else self.memory[self.memory[self.index+2]]
		return value1, value2



def get_output_signal(data, permutation):
	amps = []		
	for phase in permutation:
		amps.append(Amp(data,phase))

	result = 0
	output_signal = 0
	while True:
		for amp in amps:
			result = amp.run(result)
			if result == "Halted":
				return output_signal
		output_signal = result

	return output_signal


def find_max_thruster_signal(data):
	thruster_signals = []
	for permutation in list(itertools.permutations([5,6,7,8,9])):
		thruster_signals.append(get_output_signal(data,permutation))
		
	return max(thruster_signals)

with open('input.txt') as f:
	data = [int(value) for value in f.readline().split(",")]
	print(find_max_thruster_signal(data))

