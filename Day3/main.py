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
    
    for line in data:
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]

        same = [char for char in comp1 if char in comp2]

        sum += getPriority(same[0])
    
    return sum

if __name__ == "__main__":
    res = main()

    print(res)