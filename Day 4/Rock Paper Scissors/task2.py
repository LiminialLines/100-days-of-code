import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]

print("Approach fleshsuit! I am the venerable RPS3x. I have mastered skills that defy comprehension."
      "\nThe only domain left for me to conquer is that of luck. "
      "I will challenge you to a game of Rock, Paper, Scissors.")
input("Do you accept? ")

print("You will play. It has been decided.")
print("Choose your weapon of choice below. (Do not worry. My eyes are closed.)")

# Use numbers like the solution code
player_input = input("Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")

# Validate input
if not player_input.isdigit():
    print("You typed an invalid value. The fates frown upon you. You lose.")
    quit()

player_choice = int(player_input)

if player_choice < 0 or player_choice > 2:
    print("You typed an invalid number. The fates frown upon you. You lose.")
    quit()

print("Hmm. Interesting choice. Not that I'm paying attention or anything.\n")

robot_choice = random.randint(0, 2)

print("Are you ready to test the fates?")
print("Here we go!\nRock\nPaper\nScissors\nShoot!\n")

print("You chose:")
print(game_images[player_choice])
print(names[player_choice])

print("\nRPS3x chose:")
print(game_images[robot_choice])
print(names[robot_choice])
print()

# Winner logic (single block instead of 3 branches)
if player_choice == robot_choice:
    print("Evenly matched. I'm impressed.")
elif player_choice == 0 and robot_choice == 2:
    # Rock beats scissors
    print("What?! This can't be. Another! I demand a new round!")
elif player_choice == 2 and robot_choice == 0:
    # Scissors lose to rock
    print("Expected outcome. Still, I hoped for more..")
elif player_choice > robot_choice:
    print("What?! This can't be. Another! I demand a new round!")
else:
    print("Expected outcome. Still, I hoped for more..")