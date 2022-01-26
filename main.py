#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#picks a random word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

#ask the user to guess a letter and makes the guess lowercase.
guess = input("Guess a letter: ").lower()

#Checking if the letter the user guessed (guess) is one of the letters in the chosen_word
for letter in chosen_word:
  if guess == letter:
    print("Right")
  else:
    print("Wrong")
