import random

def check_guess(guess, secret_word):
    guess = guess.lower()  # Step 2: Convert the guess to lower case
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(secret_word):
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, secret_word)  # Step 3: Call check_guess function to check the guess
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

def main():
    secret_words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    secret_word = random.choice(secret_words)

    ask_for_input(secret_word)  # Step 4: Call ask_for_input function

if __name__ == "__main__":
    main()
