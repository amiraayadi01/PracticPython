#Draw A Game Board
#Topics:

def print_horiz_lines():
    print(" --- " * user_dim)

def print_vert_lines():
    print("|    " * (user_dim + 1))

if __name__ == "__main__":
    user_dim = int(input("What size would you like the board to be: "))

    for i in range(user_dim):
        print_horiz_lines()
        print_vert_lines()
    print_horiz_lines()


