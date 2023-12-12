import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self._word_list = word_list
        self._num_lives = num_lives
        self._list_of_guesses = []
        self._word = random.choice(self._word_list)
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))

    def _update_word_guessed(self, guess):
        for i, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[i] = guess
        self._num_letters -= 1

    def _handle_correct_guess(self, guess):
        print(f"Good guess! '{guess}' is in the word.")
        self._update_word_guessed(guess)

    def _handle_incorrect_guess(self, guess):
        self._num_lives -= 1
        print(f"Sorry, '{guess}' is not in the word.")
        print(f"You have {self._num_lives} lives left.")

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self._word:
            self._handle_correct_guess(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self._list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self._list_of_guesses.append(guess)
                break

    def display_word(self):
        return ' '.join(self._word_guessed)

    def display_guesses(self):
        return ', '.join(self._list_of_guesses)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game._num_lives == 0:
            print('You lost!')
            break
        elif game._num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

def main():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    play_game(words)

if __name__ == "__main__":
    main()
