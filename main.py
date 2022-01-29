import random

import hangman_art
print(hangman_art.logo)

import hangman_words


#picks a random word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(hangman_words.word_list)

#create variable to keep count on the number of lives/guesses a player has left
lives = 6

#testing code
print(f'Pssst, the solution is {chosen_word}.')


#created an empty list called display
display = []

#For each letter in the chosen_word, a "_" is added to 'display'
for letter in chosen_word:
  display.append("_")

 
# while loop to let the user guess again. The loop should will stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
while "_" in display and lives > 0:

#ask the user to guess a letter and makes the guess lowercase.
  guess = input("Guess a letter: ").lower()
  
  
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.  
  
   
  for spaces in range(0, len  (chosen_word)):
    if guess == chosen_word[spaces]:
      display[spaces] = guess
    
      
  if guess not in chosen_word:
    lives -= 1
    print(f"You picked {guess}, that is not in the word. You lose a life.")
    
  
  

  #Join all the elements in the list and turn it into a String
  print(f"{' '.join(display)}")
  print(hangman_art.stages[lives])

if "_" not in display and lives > 0:
  print("You Win")
elif "_" in display and lives == 0:
  print("You Lose")


