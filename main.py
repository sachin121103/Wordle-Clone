from words import word_dict
import random

def generate_word():

    """Generates the word randomly from words.py"""

    generated_word = random.choice(word_dict)
    return generated_word

def show_guess(guess_list, word_list):

    """The role of this function is to process the guess and compare it with the original word"""

    correct_letters = {letter for letter, correct in zip(guess_list, word_list) if letter == correct}
    misplaced_letters = set(guess_list) & set(word_list) - correct_letters
    wrong_letters = set(guess_list) - set(word_list)

    print(f"The correct letters are: {" ,".join(correct_letters)}")
    print(f"The misplaced letters are: {" , ".join(misplaced_letters)}")
    print(f"The wrong letters are: {" , ".join(wrong_letters)}")

def intro_game():
    """This function introduces the game itself and how it is to be played."""
    print("This game is a clone of Wordle.\nTo play, guess any valid 5 letter word. Follow the clues to get the correct word.\nYou get only 6 guesses")

GUESSES = 6 # Hard-coded. Should not change
count = 1
Word_of_the_day = generate_word()

intro_game()

while count <= GUESSES:
    word_list = list(Word_of_the_day)
    
    guess = input("\nEnter your guess here: ").upper()
    guess_list = list(guess)
    
    if guess in word_dict:
        if guess == Word_of_the_day: 
            print(f"Congrats!You got the word right in {count} guesses!")
            break
        else:
            print('\n')
            show_guess(guess_list, word_list)
            count += 1
    else:
        print("Enter a valid word")


if count > 6:
    print(f"\nYou ran out of guesses. The actual word was {Word_of_the_day}. Game Over.")
