
def getPoints(move):
    if move == "A":
        return 1
    elif move == "B":
        return 2
    else:
        return 3

def main():

    with open("data.txt", "r") as file:
        games = file.read().split("\n")

    points = 0

    for game in games:
        move = game.split()[1]
        bad = game.split()[0]

        #A for Rock, B for Paper, and C for Scissors

        if move == "X":
            #LOSE
            if bad == "A":
                points += getPoints("C")
            elif bad == "B":
                points += getPoints("A")
            else:
                points += getPoints("B")
        elif move == "Y":
            #DRAW
            points += 3
            points += getPoints(bad)
        else:
            #WIN
            points += 6
            if bad == "A":
                points += getPoints("B")
            elif bad == "B":
                points += getPoints("C")
            else:
                points += getPoints("A")
    
    return points

if __name__ == "__main__":
    res = main()
    print(res)