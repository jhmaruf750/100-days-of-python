Rock= '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper='''

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images=[Rock,Paper,Scissors]


user_choice=int(input("what do you choose?Type 0 for Rock,1 for paper or 2 for scissors"))

if user_choice>=0 and user_choice <=2:
      print(game_images[user_choice])


computer_choice=random.randint(0,2)

print("Computer chose:")

print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
   print("You typed on invalid number.you lose!")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif computer_choice==0 and user_choice==2:
    print("you lose!")

elif computer_choice>user_choice:
    print("you lose!")
elif user_choice>computer_choice:
    print("You win!")
elif computer_choice==user_choice:
    print("It's a draw!")


