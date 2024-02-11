import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            # Loop through each letter in the word
            for i, letter in enumerate(self.word):
                # Check if the letter is equal to the guess
                if letter == guess:
                    # Replace the corresponding "_" in the word_guessed with the guess
                    self.word_guessed[i] = guess

            # Reduce the variable num_letters by 1
            self.num_letters -= 1
        else:
            self.num_lives -= 1  # Step 2: Reduce num_lives by 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

hangman_game = Hangman(["banana", "mango", "passion fruit", "dragon fruit", "apple"])
hangman_game.ask_for_input()
print("The word was:", hangman_game.word)  # Print the word after the game
print("Word guessed so far:", ''.join(hangman_game.word_guessed))  # Print the word guessed so far
