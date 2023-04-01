import os

if __name__ == '__main__':
    print("welcome to robo speaker 1.1 created by yuvraj".title())
    print("this is free version you can use it 10 times in a row.".title())
    count = 0
    name = input('enter your name '.title())
    while count < 10:
        say = input("enter what you want me to speak. ".title())

        if name and say.lower() == 'hello':
            command = f'say {say} {name}'
            os.system(command)
        elif say.lower() == 'how are you?':
            os.system("say 'I,m good what about you?'")
        elif say.lower() == 'bye':
            command = f"say {say} {name}"
            os.system(command)
            quit()
        else:

            command = f"say {say}"
            os.system(command)
        count += 1
