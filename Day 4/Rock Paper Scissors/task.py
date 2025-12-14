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
choices = [rock, paper, scissors]
print("Approach fleshsuit! I am the venerable RPS3x. I have mastered skills that defy comprehension."
      "\nThe only domain left for me to conquer is that of luck. "
      "I will challenge you to a game of Rock, Paper, Scissors.")
input("Do you accept?")
print("You will play. It has been decided. Choose your weapon of choice below. \n(Do not worry. My eyes are closed.)")
player_choice = input(f"Do you choose: {rock}\nrock\n{paper}\npaper\n{scissors}\nscissors\n")
print("Hmm. Interesting choice. Not that I'm paying attention or anything.")
robot_choice = random.randint(0, 2)
print("Are you ready to test the fates?\nHere we go!\nRock\nPaper\nScissors\nShoot!")
# robot choice 0 = rock. The follow sections makes the post-game logic for winner/loser.
if robot_choice == 0:
    print(rock)
    print("rock")
    if player_choice == "rock":
        print("Evenly matched. I'm impressed.")
    elif player_choice == "paper":
        print("What?! This can't be. Another! I demand a new round!")
    else:
        print("Expected outcome. Still, I hoped for more..")
# robot choice 2 = paper
elif robot_choice == 2:
    print(paper)
    print("paper")
    if player_choice == "rock":
        print("Expected outcome. Still, I hoped for more..")
    elif player_choice == "paper":
        print("Evenly matched. I'm impressed.")
    else:
        print("What?! This can't be. Another! I demand a new round!")
# robot choice 3 = scissors
else:
    print(scissors)
    print("scissors")
    if player_choice == "rock":
        print("What?! This can't be. Another! I demand a new round!")
    elif player_choice == "paper":
        print("Expected outcome. Still, I hoped for more..")
    else:
        print("Evenly matched. I'm impressed.")
