import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_game():
    """Play the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'exit' to quit the game.")

    # Initialize score counters
    wins, losses, ties = 0, 0, 0

    while True:
        player_choice = input("Enter your choice: ").lower()
       
        # Check if the player wants to exit the game
        if player_choice == 'exit':
            print("Thanks for playing!")
            break

        # Validate player input
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Get the computer's choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(player_choice, computer_choice)

        # Update the score based on the result
        if result == 'win':
            print("You win!")
            wins += 1
        elif result == 'lose':
            print("You lose!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        # Display the current score
        print(f"Score -> Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

if __name__ == "__main__":
    play_game()