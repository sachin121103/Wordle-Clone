import contextlib
import random
from string import ascii_letters, ascii_uppercase
from words import word_dict
from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on black"}))

LETTERS = 5
GUESSES = 6

def main():
    # Pre-process
    word = get_random_word()
    guesses = ["_" * LETTERS] * GUESSES

    # Process (main loop)
    with contextlib.suppress(KeyboardInterrupt):
        for i in range(GUESSES):
            refresh_page(headline=f"Guess {i + 1}")
            show_guesses(guesses, word)

            guesses[i] = guess_word(previous_guesses=guesses[:i])
            if guesses[i] == word:
                break

    # Post-process
    game_over(guesses, word, i+1,guessed_correctly=guesses[i] == word)

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]: {headline} :[/]\n")

def get_random_word():
    """Generates the word randomly from words.py"""
    generated_word = random.choice(word_dict)
    print(generated_word)
    return generated_word

def show_guesses(guesses, word):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"

        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")

def guess_word(previous_guesses):
    guess = console.input("\nGuess word: ").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)

    if guess not in word_dict:
        console.print(
            f"Your guess is invalid. Try again", style="warning"
        )
        return guess_word(previous_guesses)
    
    return guess

def game_over(guesses, word, num_guesses, guessed_correctly):
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}. You got it in {num_guesses} guesses[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word}[/]")

if __name__ == "__main__":
    main()