import random  # Step 2: Importing the random module

# Step 1: List of 5 favorite fruits
favorite_fruits = ['Apple', 'Banana', 'Strawberry', 'Mango', 'Pineapple']

# Step 3: Selecting a random word from the word_list
word_list = favorite_fruits
word = random.choice(word_list)  # Step 4: Assigning the randomly generated word to a variable called 'word'

# Step 5: Print out the randomly chosen word
print(word)

#Task 3
# Step 1: Ask the user to enter a single letter
guess = input("Please enter a single letter: ")  # Step 2: Assign the input to a variable called 'guess'

# Display the user's input
print("You entered:", guess)

Task 4
# Step 1: Validation using if-else conditions
if len(guess) == 1 and guess.isalpha():
    # Step 2: Print "Good guess!" if the conditions are met
    print("Good guess!")
else:
    # Step 3: Print an error message if the conditions are not met
    print("Oops! That is not a valid input.")
