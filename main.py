import random
from hangman_art import logo, stages
from hangman_words import word_list

# Display the game logo at the start
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Debug: Print the chosen word
print(f'The chosen word is: {chosen_word}')

end_of_game = False
lives = 6
guessed_letters = []  # To keep track of guessed letters

# Create blanks
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'.")
    else:
        guessed_letters.append(guess)

        # Check guessed letter
        if guess in chosen_word:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else:
            lives -= 1
            print(f"'{guess}' is not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You lose.")
            else:
                # Print the hangman art corresponding to the remaining lives
                print(stages[lives])

        # Print the current state of the word with blanks and guessed letters
        print(" ".join(display))

        # Check if user has guessed all letters
        if "_" not in display:
            end_of_game = True
            print("You win.")
