#!/usr/bin/python3

class Intcode:
	def __init__(self,memory):
		self.memory = memory + [0] * 10000
		self.instruction_pointer = 0
		self.relative_base = 0

	def run(self):
		opcode, param1_mode, param2_mode, param3_mode = self._process_instruction()

		while opcode != 99:
			# addition
			if opcode == 1:
				value1, value2 = self._read_arguments(param1_mode, param2_mode)
				self.memory[self._get_index_by_param_mode(param3_mode, 3)] = value1 + value2
				self.instruction_pointer += 4
			# multiplication
			elif opcode == 2: 
				value1, value2 = self._read_arguments(param1_mode, param2_mode)
				self.memory[self._get_index_by_param_mode(param3_mode, 3)] = value1 * value2
				self.instruction_pointer += 4
			# input
			elif opcode == 3:
				self.memory[self._get_index_by_param_mode(param1_mode, 1)] = int(input("Input: "))
				self.instruction_pointer += 2
			# output
			elif opcode == 4:
				result = self.memory[self._get_index_by_param_mode(param1_mode, 1)]
				self.instruction_pointer += 2		
				print(result)
			# jump if true
			elif opcode == 5:
				value1, value2 = self._read_arguments(param1_mode, param2_mode)
				if value1 != 0:
					self.instruction_pointer = value2
				else:
					self.instruction_pointer += 3
			# jump if false
			elif opcode == 6:
				value1, value2 = self._read_arguments(param1_mode, param2_mode)
				if value1 == 0:
					self.instruction_pointer = value2
				else:
					self.instruction_pointer += 3
			# less than
			elif opcode == 7:
				value1, value2 = self._read_arguments(param1_mode, param2_mode)
				self.memory[self._get_index_by_param_mode(param3_mode, 3)] = 1 if value1 < value2 else 0
				self.instruction_pointer += 4
			# equals
			elif opcode == 8:
				value1, value2 = self._read_arguments(param1_mode, param2_mode)
				self.memory[self._get_index_by_param_mode(param3_mode, 3)] = 1 if value1 == value2 else 0
				self.instruction_pointer += 4
			# change relative base
			elif opcode == 9:
				self.relative_base += self.memory[self._get_index_by_param_mode(param1_mode, 1)]
				self.instruction_pointer += 2
			# unknown operation
			else:
				print(f'unknown opcode {opcode}')
				exit("unknown opocode")
			# process next iteration
			opcode, param1_mode, param2_mode, param3_mode = self._process_instruction()
	
		return "Halted"

	def _process_instruction(self):
		instruction = str(self.memory[self.instruction_pointer])
		instruction_length = len(instruction)
		#add leading zeros
		if instruction_length != 5:
			instruction = "0" * (5-instruction_length) + instruction
		opcode = int(instruction[3]+instruction[4])
		param1_mode = int(instruction[2])
		param2_mode = int(instruction[1])
		param3_mode = int(instruction[0])
		return opcode, param1_mode, param2_mode, param3_mode

	def _read_arguments(self,param1_mode, param2_mode):
		value1 = self.memory[self._get_index_by_param_mode(param1_mode,1)]
		value2 = self.memory[self._get_index_by_param_mode(param2_mode,2)]
		return value1, value2

	def _get_index_by_param_mode(self,param_mode, offset):
		# position mode
		if param_mode == 0:
			return self.memory[self.instruction_pointer+offset]
		# absolute mode
		elif param_mode == 1:
			return self.instruction_pointer+offset
		elif param_mode == 2:
			return self.memory[self.instruction_pointer+offset] + self.relative_base
		else:
			print(f'unknown mode {param_mode}')
			exit("unknown mode")


with open('input.txt') as f:
	data = [int(value) for value in f.readline().split(",")]
	Intcode(data).run()
	