import random


# define a function to guess a number.
# x is our number which makes the range form 1 to x example x =2 so our guess will be between 1 and 2 only
# it would be recommended to take x as big digit so that you can guess a lot of numbers.
def guess(x):
    # store random number in random_number variable.
    random_number = random.randint(1, x)
    # gues initialized to 0 so that our random number shouldn't collide.
    gues = 0
    # using attempt variable we can track how many attempts we have taken to guess the correct number.
    attempt = 0
    # till gues is not equal to random number continue the loop.
    # As we guess the number loops breaks!
    while gues != random_number:
        gues = int(input(f"guess a number between 1 and {x} ".title()))
        attempt += 1
        if gues < random_number:
            print("Sorry, guess again. Too low.")
        elif gues > random_number:
            print("Sorry, guess again. Too High.")

    print(f"Yay, congrats. You guessed the number {random_number} correctly in {attempt} attempts!!")


# now let's guess the number.
# guess(10)

# Now lets make a function program in which our computer will guess the number we want him to guess.
def Computer_guess(x):
    # define boundary low and high for computer
    low = 1
    high = x
    # feedback variable will see our response as 'h' or 'l' or 'c' to guide computer to guess correct number.
    feedback = ""
    attempt = 0
    while feedback != 'c':
        '''because high and low can't be equal so if they are
         not equal keep computer guessing else
          he knows the correct answer'''
        if low != high:
            guess = random.randint(low, high)

        else:
            guess = low
        # Guiding computer by typing h , l , c
        feedback = input(f" Is {guess}?..else type  too high (H), too low (L), or correct (C) to guide me?? ").lower()
        # Tracking computers attempts
        attempt += 1
        # h means high
        if feedback == 'h':
            high = guess - 1
        # l means low
        elif feedback == 'l':
            low = guess + 1
    # else computer guessed the answer.
    print(f'Yay ! your computer Guessed the number, {guess} Correctly!')
    print(f"Your computer taken {attempt} attempts to guess your number!!".upper())


# it would be highly recommended to give big range for more fun
# and decide the number before running the program which computer will guess from the range
Computer_guess(1000)
