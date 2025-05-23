#display art

from art import logo,vs
from data import data
import  random

def format_data(account):
    # format the account data into printable format
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name},a{account_descr},from {account_country}"


def check_answer(user_guess,a_followers,b_followers):
    """TAke the user's guess and the follower coutnts and returns if they got it right"""
    if a_followers>b_followers :
        return user_guess=="a"
    else:
        return user_guess=="b"


print(logo)
score=0

game_should_continue=True
account_b=random.choice(data)

while True:
    #generate a random account form the game data

    account_a=account_b
    account_b = random.choice(data)


    if account_a==account_b:
        account_b = random.choice(data)

    print(f"compare A:{format_data(account_a)}.")
    print(vs)
    print(f"compare B:{format_data(account_b)}.")

    #ask user for the guess

    guess=input("who has more followers?Type 'A' or 'B':").lower()
    #check if user is correct

    #get follower count of each account
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    #use if statement to check if user is correct

    is_correct=check_answer(guess,a_follower_count,b_follower_count)


    #give user feedback on their guess
    #score keeping
    if is_correct:
        score+=1
        print(f"you are right!current score {score}")
    else:
        print(f"sorry,that's wrong.Final score {score}")
        game_should_continue=False


#make the game repeatable

#making account at position B become the next account at position A.

