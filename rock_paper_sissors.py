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
choices = [rock,paper,scissors]
computer_choice = random.choice(choices)
user_choice = int(input("What do you choose? 0 Rock, 1 Paper, 2 Scissors\n"))
#if computer_choice == user_choice:
#    print("Its a tie")
if user_choice==0:
    user_choice = rock
    print(rock)
elif user_choice == 1:
    user_choice = paper
    print(paper)
else:
    user_choice = scissors
    print(scissors)
print(f"computer chose{computer_choice}")

#Result:
if user_choice == computer_choice:
    print("Its a tie")
elif user_choice == rock and computer_choice == scissors:
    print("You won")
elif user_choice == scissors and computer_choice == paper:
    print("You win")
elif user_choice == paper and computer_choice == rock:
    print("You win")
else:
    print("Computer wins")

#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.
