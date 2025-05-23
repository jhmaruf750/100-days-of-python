art='''


                    88                        88                     
                      88                        88              ,d     
                      88                        88              88     
 ,adPPYba, ,adPPYYba, 88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM  
a8"     "" ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88     
8b         ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88     
"8a,   ,aa 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,    
 `"Ybbd8"' `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888  
                                                                       
                                                                       
                        
                        
                        
                        
 ,adPPYba,  8b,dPPYba,  
a8"     "8a 88P'   "Y8  
8b       d8 88          
"8a,   ,a8" 88          
 `"YbbdP"'  88  


'''

print(art)

def add(n1,n2):
    return n1+n2



#Todo:write out the other 3 functions- subtract,multiply and divide.

def subtract (n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return  n1/n2

#Todo:add these 4 functions into a dictionary as the valurs.keys="+","-","*","/"


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,

}

def calculator():
    should_accumulate=True
    num1 = float(input("what is the first number?:"))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol=input("pick an operarion:")

        num2=float(input("what is the next number?:"))


        answer=operations[operation_symbol](num1,num2)

        print(f"{num1} {operation_symbol} {num2}={answer}")

        choice=input(f"Type 'y' to continue calculating with {answer},or Type 'n' to start a new calculator:")

        if choice=="y":
            num1=answer
        else:
            should_accumulate:False
            print("\n"*20)
            calculator()






calculator()