from random import shuffle
my_list = [' ', 'O', ' ']
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
def player_guess():
    num = int(input("Enter your guess number 0, 1 or 2: "))
    return num

def play(my_list,num):
    if my_list[num] == 'O':
        print('Won!!')
    else:
        print("Try next time!!!!")
        print(my_list)

#initialisation
my_list = ['O', ' ', ' ']
#shuffling
mixed_list = shuffle_list(my_list)
#user_guess
guess = player_guess()
#check whether won or not!!!
play(mixed_list,guess)