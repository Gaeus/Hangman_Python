import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"**************************** {lives}/6 lives LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"you've already guessed '{guess}'")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in correct_letters:
        print(f"You guessed '{guess}' that's not in the word. You lose a life.")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"**********************YOU LOSE, THE WORD WAS '{chosen_word.upper()}'**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
