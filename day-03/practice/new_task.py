
print("welcome to Treasure Island.\nYOur mission is to find the treasure ")

choose=input("left or right?")



if choose=="right":
    print("Game over")
else:
    select=input("swim or wait?")
    if select=="swim":
        print("Game over")
    else:
        sel=input("which door?")
        if sel== "blue":
            print("Game over")
        elif sel=="red":
            print("Game over")
        else:
            print("YOu win")
