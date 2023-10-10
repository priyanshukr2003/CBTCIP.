import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    while user_choice not in ['rock', 'paper', 'scissor']:
        print("Invalid choice. Please choose from 'rock', 'paper', or 'scissor'.")
        user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissor') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissor' and computer_choice == 'paper')
    ):
        return f"You win! {user_choice.capitalize()} beats {computer_choice}."
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice}."

def main():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
