import random

fruits = ["banana", "mango", "passion fruit", "dragon fruit", "apple"]
word_list = fruits

word = random.choice(word_list)

def check_guess(guess): # Step 1: Creating function.
    guess = guess.lower()  # Step 2: Convert the guess into lower case.
    if guess in word:  # Step 3: Check if the guess is in the word.
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(): # Step 1: Creating function.
    while True:
        guess = input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():  # Step 2: Check if the input is a valid guess.
            check_guess(guess)  # Step 3: Call the check_guess function to check if the guess is in the word.
            break
        else:
            print("Oops! That is not a valid input.")

ask_for_input()  # Step 4: Call the ask_for_input function to test the code.
print("The word was:", word)  # Print the guessed word after the game.
