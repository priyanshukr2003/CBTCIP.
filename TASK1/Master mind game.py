import random

def is_valid_number(num_str):
    return num_str.isdigit() and len(num_str) == 4

def generate_secret_number():
    return ''.join(random.sample('0123456789', 4))

def compare_numbers(secret_number, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

def player_guess(secret_number):
    attempts = 0
    while True:
        guess = input("Enter your guess (4-digit number): ")
        if not is_valid_number(guess):
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        attempts += 1
        bulls, cows = compare_numbers(secret_number, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            print("Congratulations! You've guessed the secret number!")
            return attempts

def main():
    print("Welcome to the Mastermind game!")

    while True:
        # Player 1 sets the secret number
        print("Player 1, set your secret 4-digit number.")
        secret_number_player1 = input("Enter a 4-digit number: ")
        if not is_valid_number(secret_number_player1):
            print("Invalid input. Please enter a 4-digit number.")
            continue

        # Player 2 guesses Player 1's secret number
        attempts_player2 = player_guess(secret_number_player1)
        print(f"Player 2 guessed the secret number in {attempts_player2} attempts!")

        # Player 2 sets the secret number
        print("Player 2, set your secret 4-digit number.")
        secret_number_player2 = input("Enter a 4-digit number: ")
        if not is_valid_number(secret_number_player2):
            print("Invalid input. Please enter a 4-digit number.")
            continue

        # Player 1 guesses Player 2's secret number
        attempts_player1 = player_guess(secret_number_player2)
        print(f"Player 1 guessed the secret number in {attempts_player1} attempts!")

        # Determine the winner
        if attempts_player1 < attempts_player2:
            print("Player 1 wins! Player 1 is crowned Mastermind!")
        elif attempts_player1 > attempts_player2:
            print("Player 2 wins! Player 2 is crowned Mastermind!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing Mastermind!")

if __name__ == "__main__":
    main()
