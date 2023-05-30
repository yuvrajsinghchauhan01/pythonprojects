import random

r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
s = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
invalid_option = '''
     _                         _
    |_|                       |_|
    | |         /^^^\         | |
   _| |_      (| "o" |)      _| |_
 _| | | | _    (_---_)    _ | | | |_ 
| | | | |' |    _| |_    | `| | | | |
\          /   /     \   \          /
 \        /  / /(. .)\ \  \        /
   \    /  / /  | . |  \ \  \    /
     \  \/ /    ||Y||    \ \/  /
       \_/      || ||      \_/
                () ()
                || ||
               ooO Ooo
               '''


def play():
    user = input("Please Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors  ")
    if user == 'r':
        print(f"User Choice:\n{r} ")
    elif user == 'p':
        print(f"User Choice:\n{p} ")
    elif user == 's':
        print(f"User Choice:\n{s} ")
    else:
        print("Invalid option")
    computer_choice = random.choice(['r', 'p', 's'])
    if user not in ['r', 'p', 's']:
        print(f"{invalid_option}")
    else:

        if computer_choice == 'r':
            print(f"Computer Choice:\n{r} ")
        elif computer_choice == 'p':
            print(f"Computer Choice:\n{p} ")
        elif computer_choice == 's':
            print(f"Computer Choice:\n{s} ")

    if user == computer_choice:
        return "it's a tie"

    # rock > Scissors, Scissors > paper and paper > rock
    if is_win(user, computer_choice):
        return 'You won!'
    return 'You Lost!'


def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())