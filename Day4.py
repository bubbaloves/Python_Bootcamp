import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

mychoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))

if mychoice >= 3 or mychoice < 0:
    print("You chose an invalid number, you lose!")
else:
    computerchoice = random.randint(0,2)

    print(game_images[mychoice])
    print("Computer chose: ")
    print(game_images[computerchoice])

    if mychoice == computerchoice:
        print("It's a draw.")
    elif mychoice == 0:
        if computerchoice == 1:
            print("You lose.")
        else:
            print("You win.")
    elif mychoice == 1:
        if computerchoice == 0:
            print("You win.")
        else:
            print("You lose.")
    elif mychoice == 2:
        if computerchoice == 0:
            print("You lose.")
        else:
            print("You win.")