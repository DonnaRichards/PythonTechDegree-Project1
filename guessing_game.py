"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
"""
  
import random

START_NUM = 1
END_NUM = 10

def play_game(bestscore):
    random_no = random.randint(START_NUM, END_NUM)
    score = 0
    guess = 0
    while guess != random_no:
        try:
            guess = int(input(f"Enter a number between {START_NUM} and {END_NUM} as your guess: "))
            if guess < START_NUM or guess > END_NUM:
                raise ValueError(f"Your guess needs to be within {START_NUM} to {END_NUM} ")
        except ValueError as err:
            print("Invalid number entered")
            print(err)
            continue
        score += 1
        if guess > random_no:
            print("Guess is too high - have another go")
        elif guess < random_no:
            print("Guess is too low - have another go")
        else:
            print("You got it !!! way to go")
            print(f"Your score is {score}")
    if score < bestscore:
        print('****** New best score  ******** ')
        bestscore = score
    return bestscore

def start_game():
    name = input("Hi there, what is your name ?  "  )
    print(f"Welcome to the game {name} !!")
    print("------------------------------")
    best_score = 99999
    play_again = "y"
    while play_again[0].lower() == 'y':
        best_score = play_game(best_score)
        play_again = input(f"Do you want to play again {name}  ? (y/n)  ")
        if play_again[0].lower() == 'y':
            print(f"Alrighty, let's go {name} !! your current best score to beat is {best_score}")
    print(f"Thanks for playing {name}, your best score was {best_score}")
    
# Kick off the program by calling the start_game function.
start_game()