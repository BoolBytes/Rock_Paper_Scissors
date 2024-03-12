# Very basic Rock, Paper, Scissors game primarily using functions conditional statements and lists
# Import 'random' module to allow the computer to select a random integer
import random


# Print statement for finding user's choice
def choices():
    return '''
    Type...
    1 for ROCK
    2 for PAPER
    3 for SCISSORS
    = '''


# Input statement storing user choice - 1 so user choice is equal to index position of the game list
def get_user_choice():
    return int(input(choices())) - 1


# Using random module to find computer choice
def get_computer_choice():
    return random.randint(1, 3) - 1


# Function to find winner taking computer and user choices as arguments
# Conditional statements used to set parameters for what a Draw, Win, and Loss is
def determine_winner(user_choice, computer_choice):
    game = [rock, paper, scissors]
    print(f"You chose:\n{game[user_choice]}")
    print(f"Computer chose:\n{game[computer_choice]}")

    if user_choice == computer_choice:
        print("DRAW")
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        print("YOU WIN")
    else:
        print("YOU LOSE")


# Defining primary flow of code
def main():
    user_choice = get_user_choice()
    os_choice = get_computer_choice()
    determine_winner(user_choice, os_choice)


# ASCII characters to represent Rock, Paper, and Scissors for enhance UX
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Entry point
if __name__ == "__main__":
    main()  