#!/usr/bin/env python3

def run(memory, verb, noun):
    index = 0
    memory[1] = verb
    memory[2] = noun
    opcode = memory[index]
    while opcode != 99:
        position1 = memory[index+1]
        position2 = memory[index+2]
        position3 = memory[index+3]
        value1 = memory[position1]
        value2 = memory[position2]
        
        if (opcode == 1):
            memory[position3] = value1 + value2
        elif (opcode == 2): 
            memory[position3] = value1 * value2
        else:
            exit('unknown opcode', opcode)

        index += 4
        opcode = memory[index]
    
    
    return memory[0]



with open('input.txt') as f:
    input = [int(value) for value in f.readline().split(",")]
    for noun in range(0,100):
        for verb in range(0,100):
            result = run(input.copy(), noun, verb)
            if(result == 19690720):
                print(100 * noun + verb)
                exit()
