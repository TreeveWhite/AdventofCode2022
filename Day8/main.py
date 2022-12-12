
def get_up_trees_down(trees, x, y):
    result = []
    for a in range(len(trees)):
        if a <= y:
            continue
        for b in range(len(trees[a])):
            if b == x:
                result.append(trees[a][b])
    
    return result

def get_up_trees_up(trees, x, y):
    result = []
    for a in range(len(trees)):
        if a >= y:
            break
        for b in range(len(trees[a])):
            if b == x:
                result.append(trees[a][b])
    
    return result


def main():
    
    with open("data.txt", "r") as file:
        data = file.read().replace("\n\n", "\n").split()
    
    trees = []
    for line in data:
        trees.append(list(map(int, list(line))))

    total = 0
    
    for y in range(len(trees)):
        for x, tree in enumerate(trees[y]):
            print(f"{tree} - {x} {y}")
            #Edge
            if (x == 0) or (x == len(trees[y])-1) or (y == 0) or (y == len(trees)-1):
                total += 1
                print("e\n")
                continue

            #Not Visible UP
            if all(trees[y][x] > otherTree for otherTree in get_up_trees_up(trees, x, y)):
                total += 1
                print("u\n")

            #Visible Down
            elif all(trees[y][x] > otherTree for otherTree in get_up_trees_down(trees, x, y)):
                total += 1
                print("d\n")

            #Visible Left
            elif all(trees[y][x] > otherTree for otherTree in trees[y][:x]):
                total += 1
                print("l\n")

            #Visible Right
            elif all(trees[y][x] > otherTree for otherTree in trees[y][x+1:]):
                total += 1
                print("r\n")


    return total



if __name__ == "__main__":

    resp = main()

    print(resp)
