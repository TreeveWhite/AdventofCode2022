def main():
    
    with open("elves.txt", "r") as file:
        data = file.read()

    elves_unformat = data.split("\n\n")
    
    elves_data = []

    for elf in elves_unformat:
        elves_data.append(elf.split("\n"))

    top_elves = []
    total = 0

    for i in range(3):

        highest_elf = None
        highest_elf_total = 0

        for elf in elves_data:
            sum = 0

            for item in elf:
                sum += int(item)

            if sum > highest_elf_total:
                highest_elf_total = sum
                highest_elf = elves_data.index(elf) + 1
        
        top_elves.append(highest_elf)
        total += highest_elf_total

        elves_data.pop(highest_elf-1)
    
    return top_elves, total
    

if __name__ == "__main__":
    top = main()

    print(f"3 Elves With Most Calories: {top[0]}")
    print(f"Total Calories: {top[1]}")
