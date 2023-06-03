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
      #import random module
import random

#Create a word list of your choice
word_list = ['ardverk', 'baboon', 'camel', 'gorrila', 'hero', 'productive',
             'smart', 'focus', 'meditation', 'calm', 'wealth', 'skillful',
             'polymath', 'revise', 'learn', 'neverbackdown', 'leader', 'healthy']
#define a variable containting random word
choosen_word = random.choice(word_list)
#create an empty list
display = []
# ADD '_' in till length of the word
for letter in choosen_word:
    display.append('_')
print(display)
#Variable contain lives of player
lives = 6
#Run the loop till all length of word.
while lives > 0:
    user_guess = input('Enter a letter: ').lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == user_guess:
            display[position] = letter
    print(display)
    #if the player guess is not correct 1 live will taken away....
    if user_guess not in choosen_word:
        lives -= 1
        print(f'You have {lives} lives now')
#if '_' not in list that means you won else you lost...
if '_' not in display:
    print('YOU WON!!!!!!')
else:
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
    print('GAME OVER :(')
