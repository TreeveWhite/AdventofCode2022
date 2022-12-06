import re

def format_crates(lines, num_crates=9):
    resp = []

    for i in range(num_crates):
        resp.append([])
    
    for line in lines:
        i = 0
        for char in line[1::4]:
            if char != ' ':
                resp[i].append(char)
            i += 1

    return resp

def format_instructions(lines):
    inst = []

    for line in lines:
        result = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)\n?", line)

        result.groups()

        inst.append([int(result.group(1)), int(result.group(2))-1, int(result.group(3))-1])

    return inst

def apply_inst(inst, crates):
    for i in range(inst[0]):
        crates[inst[2]].insert(i, crates[inst[1]][i])
    
    for i in range(inst[0]):
        crates[inst[1]].pop(0)
    
    return crates

def print_crates(crates):
    for crate in crates:
        print(crate)

def main():
    
    with open("data.txt", "r") as file:
        data = file.readlines()

    crates_data = format_crates(data[:8])

    instructions = format_instructions(data[10:])

    for inst in instructions:
        crates_data = apply_inst(inst, crates_data)
        
    return crates_data

if __name__ == "__main__":

    resp = main()

    print_crates(resp)