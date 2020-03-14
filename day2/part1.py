#!/usr/bin/env python3

def run(tape):
    index = 0
    opcode = tape[index]
    while opcode != 99:
        position1 = tape[index+1]
        position2 = tape[index+2]
        position3 = tape[index+3]
        value1 = tape[position1]
        value2 = tape[position2]
        
        if (opcode == 1):
            tape[position3] = value1 + value2
        elif (opcode == 2): 
            tape[position3] = value1 * value2
        else:
            exit('unknown opcode', opcode)

        index += 4
        opcode = tape[index]
    
    
    return tape[0]



with open('input.txt') as f:
    input = [int(value) for value in f.readline().split(",")]
    result = run(input)
    print(result)
