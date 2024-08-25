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

rps = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

#Player decision
player_choice = rps[int(input())]
print(player_choice)

#Computer decision
computer_choice = rps[random.randint(0,2)]
print(f"Computer Chose: \n {computer_choice}")

if player_choice == computer_choice:
    print("It is a Draw")
elif player_choice == rock and computer_choice == scissors:
    print("You Win")
elif player_choice == scissors and computer_choice == paper:
    print("You Win")
elif player_choice == paper and computer_choice == rock:
    print("You Win")
else:
    print("You Loose")
