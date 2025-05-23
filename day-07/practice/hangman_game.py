hangman_stages = [
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """
]




word_list=["maruf","maria","mahid"]

import random

lives=6

chosen_word=random.choice(word_list)

print(chosen_word)

placeholder=""

word_length=len(chosen_word)

for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over=False

correct_letters=[]

while  not game_over:
    print(f"{lives}/6 Lives left!")

    guess=input("guess a letter:").lower()

    if guess in correct_letters:
        print(f"you've already guess{guess}")
    display=""

    for letter in chosen_word:
      if letter==guess:
          display+=letter
          correct_letters.append(letter)
      elif letter in correct_letters:
          display+=letter
      else:
          display+="_"

    print(display)

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess},that's a not in the word.you lose a life!")
        if lives==0:
            game_over=True
            print(f"It was {chosen_word}..YOu lose!")

    if "_" not in display:
        game_over=True
        print("You win!")


    print(hangman_stages[lives])
