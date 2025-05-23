import random

art='''

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/    


'''

print()

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score==c_score: return "Draw"
    elif c_score==0:
        return "Lose,opponent has Blackjack"
    elif u_score==0:
        return "win with a Blackjack"
    elif u_score>21:
        return "YOu went over.YOu lose"
    elif c_score>21:
        return "Opponent went over.You win"
    elif u_score>c_score:
        return "YOu win"
    else:
        return "You lose"

def play_game():

    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())



    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"your cards:{user_card},current score:{user_score}")
        print(f"computer's first cards: {computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True

        else:
            user_should_deal=input("Type 'y' to get another card,type 'n' to pass:")
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True


    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(f"Your final hand:{user_card},final score:{user_score}")
    print(f"Your final hand:{computer_card},final score:{computer_card}")

    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack?Type 'y' or 'n'")=="y":
    print("\n"*20)
    play_game()









