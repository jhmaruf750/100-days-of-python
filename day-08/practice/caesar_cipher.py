logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(logo)



import string
alphabets = list(string.ascii_lowercase)




# def encrypt(original_text,shift_amount):
#     cipher_text=""
#
#     for letter in original_text:
#         shifted_position=alphabets.index(letter)+shift_amount
#
#         shifted_position%=len(alphabets)
#         cipher_text+=alphabets[shifted_position]
#
#     print(f"Here is the encoded result:{cipher_text}")


# def decrypt(original_text,shift_amount):
#     output_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabets.index(letter) - shift_amount
#
#         shifted_position %= len(alphabets)
#         output_text += alphabets[shifted_position]
#
#     print(f"Here is the encoded result:{output_text}")


def ceaser(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabets:
            output_text+=letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount

            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]

    print(f"Here is the {encode_or_decode}d result:{output_text}")

should_continue=True

while should_continue:

    direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))



# decrypt(original_text=text,shift_amount=shift)
# encrypt(original_text=text,shift_amount=shift)

    ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart=input("Type 'yes if you want to go again.otherwise type 'no'.\n").lower()
    if restart=="no":
        should_continue=False
        print("Goodbyee!!")

