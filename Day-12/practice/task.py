enemies=1

def increse_enemies():
    enemies=2
    print(f"enimies inside function{enemies}")


increse_enemies()
print(f"enimies outside function:{enemies}")


#local scope

def drink_potion():
    potion_strenth=2
    print(potion_strenth)


drink_potion()
# print(potion_strenth) #not accectablle


#global scope
player_health=3  #always acceptable inside or outside

#There is no block scope in python
enemy=["skeleton","zombie","alien"]
game_level=10
def create_enemy():

    new_enemy=""
    if game_level<5:
        new_enemy=enemy[0]

    print(new_enemy)