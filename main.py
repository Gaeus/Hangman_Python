import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print("debug:",chosen_word)

placeholder = ["_" for symbol in chosen_word ] # EXPRESSION for ITEM in ITERABLE
display = ("".join(placeholder))
print(display)


game_over = False
correct_guesses = [] # outside the loop so it isn't wiped by each loop

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("you won!")
