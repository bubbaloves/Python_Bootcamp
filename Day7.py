import random
import Day7_hangmanArt
import Day7_hangmanWords

#Chose word and create variables
chosen_word = random.choice(Day7_hangmanWords.word_list)
wordlen = len(chosen_word)
end_of_game = False
display = []
lives = 6

#Logo for beginning of game
print(Day7_hangmanArt.logo)
print(chosen_word)

#Creating blank word
for _ in range(wordlen):
    display += "_"

#Play game
while not end_of_game: 
    #Guess letter
    guess = input("Please guess a letter: ").lower()

    #Did player already guess this letter
    if guess in display:
        print(f"The letter {guess} was already guessed.")

    #If guessed letter correctly
    for position in range(wordlen):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #If guessed letter incorrectly
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
        else:
            print(f"The letter {guess} is not in the word. You lose a life.")

    #Display final string at end of game
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    #Print Hangman Art at correct stage of game
    print(Day7_hangmanArt.stages[lives])  