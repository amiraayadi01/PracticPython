#Rock Paper Scissors

player1_input = int(input("Enter 1 for Rock, Enter 2 for Paper, Enter 3 for Scissors"))
player2_input = int(input("Enter 1 for Rock, Enter 2 for Paper, Enter 3 for Scissors"))
if player1_input == 1 and player2_input == 3:
    print("Player 1 Won")
elif player1_input == 2 and player2_input == 1:
    print("Player 2 Won")
