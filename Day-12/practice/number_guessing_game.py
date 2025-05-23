import art
from random import randint


print(art.logo)

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURN=5




#funtion to check user's guess aginst actual answer

def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too high...")
        return turns-1
    elif user_guess<actual_answer:
        print("Too Low...")
        return turns-1
    else:
        print(f"you got it!The answer was {actual_answer}")

#make a function to set difficulty

def set_difficulty():
    level=input("choose a difficulty.Type 'easy' or 'hard':")

    if level=="easy":

        return EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURN

def game():
    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessng Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer=randint(1,100)


    turns=set_difficulty()



    guess=0

    while guess!=answer:
        print(f"you have {turns} attemps remaining to guess the number")
        #let the user guess

        guess=int(input("make a guess:"))

        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of guesses,you lose....")
            return

        elif guess!=answer:
            print("Guess again!")




#Track the number of turns and reduce by 1 if they get it wrong

#Repeat the guessing functionality if they get it wrong


game()