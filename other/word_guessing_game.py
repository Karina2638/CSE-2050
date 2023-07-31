import random

play_again = True
while play_again:

    numero = random.randrange(1, 9)
    words = ['elephant', 'panther', 'strawberry', 'cicada', 'halogen', 'printer', 'asphalt', 'permutation', 'lingering']
    word = words[numero]
    it = [] # this list does the underscore thing
    turns = 0
    won = False

    for i in range(len(word)): # sets up the underscores in the list
        it.append('_')

    print('You have 15 turns to find the word. Good luck!')
    for i in it: # prints out the list aesthetically
        print(i, end='')
    print('\n')

    while turns < 15 and not won: # counts turns
        guess = input()
        for count, letter in enumerate(word): # goes through each letter in the word
            if guess == letter: # checks if the input is the same as the letter being tested
                it[count] = letter # updates list letter based on list index counter
            
        turns += 1
        print(f'turns completed: {turns}/15')

        if '_' not in it:
            won = True


        for i in it: # prints out the list aesthetically
            print(i, end='')
        print('\n')

    if won:
        print('Congratulations! You guessed the correct word!')
    else:
        print(f'Out of turns! The word was {word}.')

    print('Play again? Type [y] or [n].')
    yes = input()
    if yes == 'y':
        play_again = True
    else:
        play_again = False