from words import word_dict

GUESSES = 6 # Hard-coded. Should not change
count = 1
Word_of_the_day = 'AWASH'

while count <= GUESSES:
    word_list = list(Word_of_the_day) # ['A', 'W', 'A', 'S', 'H']
    
    guess = input("\nEnter your guess here: ").upper()
    guess_list = list(guess)
    
    if guess in word_dict:
        if guess == Word_of_the_day: 
            print(f"You got the word right in {count} guesses")
            break
        else:
            print('\n')
            for i in range(0,len(word_list)):
                if guess_list[i] == word_list[i]:
                    print(f"The letter {word_list[i]} is in the main word at the position {i+1}")
                elif guess_list[i] in word_list:
                    print(f"The letter {guess_list[i]} is in the main word at a different position")
                else:
                    print(f"The letter {guess_list[i]} is not in the main word")
            
            count += 1
    else:
        print("Enter a valid word")

    

if count >= 6:
    print("\nYou ran out of guesses. Game Over.")
