GUESSES = 6 # Hard-coded. Should not change
count = 1
Word_of_the_day = 'CRANE'

while count <= GUESSES:
    word_list = list(Word_of_the_day)
    
    guess = input("Enter your guess here: ").upper()
    guess_list = list(guess)
    
    if len(guess_list)== 5:
        if guess == Word_of_the_day: 
            print(f"You got the word right in {count} guesses")
            break
        else:
            for i in range(0,len(word_list)):
                if word_list[i] == guess_list[i]:
                    print(f"The letter {word_list[i]} is in the main word")
                else:
                    print(f"The letter {guess_list[i]} is not in the main word")
            
            count += 1
    else:
        print("Enter a 5 letter word")

    

    