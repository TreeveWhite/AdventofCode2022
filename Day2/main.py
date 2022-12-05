
def main():

    #X for Rock, Y for Paper, and Z for Scissors
    #A for Rock, B for Paper, and C for Scissors

    with open("data.txt", "r") as file:
        games = file.read().replace("X", "A").replace("Y", "B").replace("Z", "C").split("\n")

    points = 0

    for game in games:
        player = game.split()[1]
        bad = game.split()[0]

        if player == bad:
            #draw
            points += 3
        elif player == "A" and bad == "C":
            #ROCK BEATS SICCORS
            points += 6
        elif player == "B" and bad == "A":
            #PAPPER BEETS ROCK
            points += 6
        elif player == "C" and bad == "B":
            #sissors beats paper
            points += 6
        else:
            #LOSS
            points += 0
        
        #Player Points
        if player == "A":
            points += 1
        elif player == "B":
            points += 2
        else:
            points += 3
    
    return points

if __name__ == "__main__":
    res = main()
    print(res)