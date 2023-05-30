#Suppose you're Monkey D. Luffy and you're searching for one piece treasure.
print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("welcome to treasure island.".upper())
question1 = input("you're on a strange island, you see two path which one will you choose? left or right? ".capitalize())
if question1.lower()=='left':
    question2 = input("you see a crater lake how will you cross? swim or boat ".capitalize())
    if question2.lower() == 'boat':
        question3 = input("you see two caves which one will choose? cave1 or cave2 ".capitalize())
        if question3.lower == 'cave1':
            print("wrong cave!!!! GAME OVER.".capitalize())
        else:
            print("Wohooo!! you found the tresure of one piece. ".capitalize())
    else:
        print("Sea serpent is waiting for you, GAME OVER.".capitalize())
else:
    print("You meet teach and lost the battle, GAME OVER".capitalize())
