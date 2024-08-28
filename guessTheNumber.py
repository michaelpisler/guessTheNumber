import random

def guess_the_number():
    # The computer randomly selects a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while not guessed_correctly:
        try:
            # Ask the user to input a guess
            guess = int(input("Enter your guess: "))
            number_of_attempts += 1

            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")
                guessed_correctly = True

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()