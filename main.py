#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#picks a random word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

#testing code
print(f'Pssst, the solution is {chosen_word}.')


#created an empty list called display
display = []

#For each letter in the chosen_word, a "_" is added to 'display'
for letter in chosen_word:
  display.append("_")

#converts choosen word into a list
list_word = list(chosen_word)

while not display == list_word:
  
# while loop to let the user guess again. The loop should will stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").

#ask the user to guess a letter and makes the guess lowercase.
  guess = input("Guess a letter: ").lower()


#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  for spaces in range(0, len  (chosen_word)):
    if guess == chosen_word[spaces]:
      display[spaces] = guess
    

  print(display)
if display == list_word:
  print("You Win")

