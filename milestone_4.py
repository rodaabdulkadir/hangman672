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

def main():
    # Example usage of the Hangman class
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    game = Hangman(words)

    print("Word to guess:", game.display_word())
    print("Number of unique letters:", game.num_letters)
    print("Number of lives:", game.num_lives)
    print("List of guesses:", game.display_guesses())

if __name__ == "__main__":
    main()
