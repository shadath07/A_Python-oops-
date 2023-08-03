# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...

# Write a python code to read the file and store the words in the list

# Write a function to guess a word randomly from the list.

# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter. 
# Display  letters in the clue word that were guessed correctly. 

# Let say word is EVAPORATE

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.

# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.


# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.



def read_store_word(file):
    with open(file, 'r') as file:
        words = [line.strip() for line in file]
    return words

import random
def choose_random_word(words_list):
    return random.choice(words_list)

def hangman_game():
    file_path = "Hangman.txt"
    words_list = read_store_word(file_path)

    while True:
        chosen_word = choose_random_word(words_list)
        guessed_letters = set()
        attempts = 6

        print("Welcome to Hangman!")
        clue = ['_' for _ in chosen_word]
        print(' '.join(clue))

        while attempts > 0:
            guess = input("Guess your letter: ").upper()

            if guess in guessed_letters:
                print("You already guessed this letter. Try again.")
                continue
            
            guessed_letters.add(guess)

            if guess in chosen_word:
                for i, letter in enumerate(chosen_word):
                    if letter == guess:
                        clue[i] = guess
                print(' '.join(clue))
                if '_' not in clue:
                    print("Congratulations! You guessed the word:", chosen_word)
                    break
            else:
                attempts -= 1
                print("Incorrect!")
                print(f"You have {attempts} chances left to guess.")

        else:
            print("Sorry, you ran out of attempts. The word was:", chosen_word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
if __name__ == "__main__":
    hangman_game()
