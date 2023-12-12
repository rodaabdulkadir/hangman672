import random

def get_user_input():
    # Function to get valid user input
    while True:
        guess = input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops! That is not a valid input. Please enter a single alphabetical character.")

def select_random_word(word_list):
    # Function to select a random word from the word list
    return random.choice(word_list)

def main():
    # List of favorite fruits
    favorite_fruits = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple']
    
    # Get valid user input
    user_guess = get_user_input()
    
    # Select a random word from the list
    random_word = select_random_word(favorite_fruits)
    
    # Display the randomly chosen word and the user's guess
    print("Randomly chosen word:", random_word)
    print("Your guess:", user_guess)

if __name__ == "__main__":
    main()
