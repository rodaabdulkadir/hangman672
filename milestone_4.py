import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))

    def display_word(self):
        return ' '.join(self.word_guessed)

    def display_guesses(self):
        return ', '.join(self.list_of_guesses)

    def check_guess(self, guess):
        guess = guess.lower()  # Convert guessed letter to lowercase
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  # Replace '_' in word_guessed with guess
            self.num_letters -= 1  # Reduce num_letters by 1 after correct guess
        else:
            self.num_lives -= 1  # Step 2: Reduce num_lives by 1 if guess is incorrect
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:  # Create a while loop
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  # Call the check_guess method
                self.list_of_guesses.append(guess)  # Append guess to list_of_guesses
                break  # Exit loop after successful guess

def main():
    # Example usage of the Hangman class
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    game = Hangman(words)

    game.ask_for_input()  # Call the ask_for_input method
    print("Word after guess:", game.display_word())

if __name__ == "__main__":
    main()
