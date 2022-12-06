
def get_marker(marker_length, message):
    num_char = 0

    while num_char <= len(message)-marker_length:
        chars = {message[num_char]}

        for i in range(1, marker_length):
            chars.add(message[num_char+i])

        if len(chars) == marker_length:
            break
        else:
            num_char += 1

    return num_char + marker_length

def main():

    with open("data.txt", "r") as file:
        data = file.read()
    
    #return get_marker(4, data)

    return get_marker(14, data)

if __name__ == "__main__":
    print(main())
