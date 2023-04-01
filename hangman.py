import random
import string

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

''')


def import_words():
    # randomly chooses something from the list
    words = random.choice(open('gistfile1.txt').readlines())
    if '\n' in words:
        words = words.replace('\n',"")
    print(words)

    return words.upper()


def hangman():
    word = import_words()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6

#     # getting user input
    while len(word_letters) >0 and lives > 0:
        #letters used
        print('You have', lives, 'lives left and You have used these letters: ', " ".join(used_letters))

        # what current word is i.e (F__B_E == FEEBLE)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # takes away a life if wrong
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print('Invalid character. Please try again')

# while the length of words getter than 0 iterate and lives getter than 0
    if lives == 0:
        print('''
        
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .

        ''')
        print(f'You died, sorry. The word was {word}')
    else:
        print(f"yay boi, You guessed the word {word}!!")
hangman()