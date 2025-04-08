import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print("debug:",chosen_word)

placeholder = ["_" for symbol in chosen_word ] # EXPRESSION for ITEM in ITERABLE
print ("".join(placeholder))

guess = input("Guess a letter: ").lower()


display = []
for letter in chosen_word:
    if letter == guess: # == means trully identical
        display.append(letter) #j'injecte la lettre correcte dans l'array display
    else:
        display.append("_")

print("".join(display))

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
