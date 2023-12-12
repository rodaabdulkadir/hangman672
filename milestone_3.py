import random

def get_valid_letter():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def check_guess_in_word(guess, secret_word):
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def main():
    # List of secret words (you can replace this with your own list)
    secret_words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    
    # Choose a random word from the list
    secret_word = random.choice(secret_words)

    while True:
        user_guess = get_valid_letter()
        check_guess_in_word(user_guess, secret_word)
        break  # For demonstration purposes; replace this with your intended logic

if __name__ == "__main__":
    main()
