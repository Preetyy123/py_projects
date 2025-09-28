#************************************************************************************************************************
# 8Fake Headline Generator
#import random module
"""import random

#create list for subject, actions, and places
Subjects = [
    "Prime Minister",
    "Imran Khan",
    "Soorya",
    "A group of monkey",
    "Spiderman"

]
Actions = [
    "Play footbal",
    "eating banana",
    "changes a clothes",
    "fighting",
    "have gossiping"
]
Places = [
    "at London",
    "at Eifel Tower",
    "at Taj Mahel",
    "at Washroom",
    "at home"
]
#print the random headline in while loop.
while True:
    subject = random.choice(Subjects)
    action = random.choice(Actions)
    places = random.choice(Places)

    headline = f"BREAKING NEWS: {subject} {action} {places}"
    print("\n" + headline)
    newHead = input("You you want another fake headline? (Yes/No)").strip().lower()
    if newHead == "no":
        break

print("Thankyou for generating fake headlines, We will see you soon")"""

#*************************************************************************************************************************
# Create a program which can calculate, can show history, can clear history, can append, can exit.
"""Calculator1 = "history.txt"

#create a function which can read the file and show us the history
def show_hist():
    File = open(Calculator1, 'r')
    lines = File.readlines()
    if len(lines) == 0:
        print('No History Found, Thanks.')
        
    else:
        for line in reversed(lines):
            print(line.strip())
    File.close()

#Create a function which can clear the history.
def clear_hist():
    File = open(Calculator1, 'w').close()
    print('History Cleared, Thanks.')

def update_hist(equation, result):
    File = open(Calculator1, 'a')
    File.write(equation + '=' + str(result) + '\n')
    File.close()

#Write a function which calculates the equation.
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input, Please Try Again and Use 3 input (e.g: 8+8.)")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num1 + num2
    
    elif op == '-':
        result = num1 - num2

    elif op == '*':
        result = num1 * num2

    elif op == '/':
        if num2 == 0:
            print("Please Enter the Valid Operator. Can not divide by Zero0: ")
            return
        result = num1 / num2

    else:
        print('Invalid Operator.')
        return

    if int(result) == result:
        result = int(result)
    print("Final Result:", result)
    update_hist(user_input, result)

def main():
    user_input = input("WELCOME\nYou can Calculate, Show History, Clear History, and Exit:").strip().title
    while True:
        if user_input == 'Exit':
            print("GoodBye, See You Soon")
            break

        elif user_input == 'Show History':
            show_hist()

        elif user_input == 'Clear History':
            clear_hist()

        elif user_input == 'Calculate':
            calculate(user_input)

main()"""

#**************************************************************************************************************************
# Creat a program where computer takes the secret password and user needs to guess it letter by letter, tell the user that 
# how far or how close their guess is. and counts the attempts too.

""""import random

print('Welcome to the Game.\nRules: Choose difficulty level. Easy | Medium | Hard.\nGuess the word letter by letter.\nBest of Luck')

Easy_Words = ['shorts', 'oky234', 'done246', 'hello99']
Med_Words = ['1234333', 'BlueSky25', 'Book234', 'Tiger78']
Hard_Words = ['Qm82Fp7tX', 'aZ9xY6pQr', 'Teena', 'D3jLp9zQ8']

Level = input('Pls choose Difficulty Level:').lower()
if Level == 'easy':
    secret = random.choice(Easy_Words)

elif Level == 'medium':
    secret = random.choice(Med_Words)

elif Level == 'hard':
    secret = random.choice(Hard_Words)

else:
    print('Invalid Choice, By default Easy Level Selected.')
    secret = random.choice(Easy_Words)

i = 0
while True:
    guess = input('Guess:')
    i += 1

    if guess.lower() == secret.lower():
        print(f'Congratulations You guessed it right in {i} attempts.')
        break

    hint = ''
    for j in range(len(secret)):
        if j < len(guess) and guess[j] == secret[j]:
            hint += guess[j]
        
        else:
            hint += "_"

    print('Hint', hint)
print('Game Over.')"""

#*******************************************************************************************************************************
#create a simple qrcode by importing qrcode module. #installed pillow module to save it in png format.
"""import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=TVB920h0u4g&t=1963s")
img.save("YJHD.png")"""

#Make a advanced QRcode with some formatting.
import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.ERROR_CORRECT_H,
                   box_size=10, border=4)   #this QRCode holds the formatting
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='blue')
img.save("Python Projects.png")