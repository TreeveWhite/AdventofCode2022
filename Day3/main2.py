def getPriority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def main():
    x = getPriority("A")

    with open("data.txt", "r") as file:
        data = file.readlines()

    sum = 0

    i = 0
   
    while i <= (len(data)-3):
        elf1 = data[i]
        elf2 = data[i+1]
        elf3 = data[i+2]

        same = [char for char in elf1 if char in elf2 and char in elf3]

        print(same[0])

        sum += getPriority(same[0])

        i += 3
    
    return sum

if __name__ == "__main__":
    res = main()

    print(res)