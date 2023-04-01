print("Welcome to my computer quiz!".title())
# asking users if they want to play the game or not.
playing = input("Do you want to play? ")
if playing.lower() == 'yes':
    print("Okay let's play... ".title())
else:
    quit()
# score variable will track all the points for right answers.
score = 0
# start asking questions.
question_1 = input("What does Cpu stands for? ")
if question_1.lower() == 'central processing unit':
    print('correct!!'.title())
    score += 1
else:
    print("Whoops incorrect!!".title())
question_2 = input("what is the perimeter of a rectangle? ")
if question_2.lower() == '2*(l+b)':
    print('correct!!'.title())
    score += 1
else:
    print('whoops.. incorrect!!'.title())
question_3 = int(input('How many Mb(Megabyte) is there in 1 Gigabyte? '))
if question_3 == 1024:
    print("correct!!".title())
    score += 1
else:
    print('whoops.. incorrect!!'.title())

question_4 = input("what does GPU stands for? ")
if question_4.lower() == 'graphics processing unit':
    print('correct!!'.title())
    score += 1
else:
    print('Whoops.. incorrect!!'.title())
# find the percentage
percentage = (score/4)*100
print("-"*100)

# finally printing how many scores does the user got.
print(f"You got {score} correct answers out of 4 questions and your percentage is {int(percentage)}%")



