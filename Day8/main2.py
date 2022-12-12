
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

    if len(result) != 0:
        result = result[::-1]

    return result


def main():
    
    with open("data.txt", "r") as file:
        data = file.read().replace("\n\n", "\n").split()
    
    trees = []
    for line in data:
        trees.append(list(map(int, list(line))))

    highest_score = 0
    
    for y in range(len(trees)):
        for x, tree in enumerate(trees[y]):

            print("UP")
            print(get_up_trees_up(trees, x, y))
            if len(get_up_trees_up(trees, x, y)) == 0:
                tUp = 1
            else:
                tUp = 0
                for otherTree in get_up_trees_up(trees, x, y):
                    if not trees[y][x] > otherTree:
                        break
                    tUp += 1
            print(tUp)

            #Visible Down
            
            print("DOWN")
            print(get_up_trees_down(trees, x, y))
            if len(get_up_trees_down(trees, x, y)) == 0:
                tD = 1
            else:
                tD = 0
                for otherTree in get_up_trees_down(trees, x, y):
                    if not trees[y][x] > otherTree:
                        break
                    tD += 1
            print(tD)

            #Visible Left
            tL = 1
            print("LEFT")
            left = (trees[y][:x])
            left.reverse()
            print(left)
            if len(left) == 0:
                tL = 1
            else:
                tL = 0
                for otherTree in left:
                    if not trees[y][x] > otherTree:
                        break
                    tL += 1
            print(tL)

            #Visible Right
            print("RIGHT")
            print(trees[y][x+1:])
            if len(trees[y][x+1:]) == 0:
                tR = 1
            else:
                tR = 0
                for otherTree in trees[y][x+1:]:
                    if not trees[y][x] > otherTree:
                        break
                    tR += 1
                print(tR)

            score = tUp * tD * tR * tL

            print(f"TREE SCORE {score}")

            if score >= highest_score:
                highest_score = score

    return highest_score



if __name__ == "__main__":

    resp = main()

    print(resp)
