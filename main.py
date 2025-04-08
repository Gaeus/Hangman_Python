import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel", "cookie", "praline", "cindy", "maxime"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list).lower()
# print(chosen_word) #debug

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

print(stages[lives])

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives = lives - 1

    print(display)
    # print(lives) #debug

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win.")

    if lives == 0:
        game_over = True
        print("You lost!")
