
def parse_input(lines):
    data = []

    for line in lines:

    return data

def main():

    with open("data.txt", "r") as file:
        text = file.readlines()
    
    data = parse_input(text)


if __name__ == "__main__":
    resp = main()

    print(resp)