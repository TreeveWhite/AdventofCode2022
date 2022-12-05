
def format(line):
    e1, e2 = line.strip().split(",")

    e1_values = list(map(int, e1.split("-")))
    e2_values = list(map(int, e2.split("-")))

    e1 = []

    for i in range(e1_values[1] - e1_values[0]+1):
        e1.append(e1_values[0]+i)
    
    if e1_values[1] - e1_values[0] == 0:
        e1.append(e1_values[0])
    
    e2 = []

    for i in range(e2_values[1] - e2_values[0]+1):
        e2.append(e2_values[0]+i)
    
    if e2_values[1] - e2_values[0] == 0:
        e2.append(e2_values[0])

    print(e1)

    print(e2)

    return e1, e2


    

def main():

    with open("data.txt", "r") as file:
        lines = file.readlines()

    total = 0

    for line in lines:

        elf1, elf2 = format(line)

        # print(elf1, "\n", elf2)

        for e in elf1:
            if e in elf2:
                total += 1
                # print("*")
                break

    return total
        

if __name__ == "__main__":
    resp = main()

    print(resp)
