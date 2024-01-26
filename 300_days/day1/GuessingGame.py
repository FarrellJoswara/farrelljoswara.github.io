import random
import os
import time

def createGuessMap(lower,upper):
    size=upper-lower+1
    map = [[list('-'*size)],[lower,upper]]
    return map

def guessMapUpdate(map,guess):
    lower = map[1][0]
    map[0][0][guess-lower] = guess

def printGuessMap(map):
    lower = map[1][0]-1
    upper = map[1][1]+1
    word =str(lower)+ ' <'  
    for i in map[0][0]:
        word += ' ' + str(i) + ' '
    print(word+'> '+str(upper))

run = True

os.system('cls')
print("welcome to guess the number! type q at any point to leave")

while run == True:
    valid = False
    while valid == False:
        lower_bound = random.randint(0,9)*10
        upper_bound = random.randint(lower_bound/10,10)*10
        answer = random.randint(lower_bound,upper_bound)
        guessMap = createGuessMap(lower_bound,upper_bound)
        if lower_bound != upper_bound:
            valid = True
    
    guessing_status = True


    print(f"Im thinking of a number from {lower_bound} to {upper_bound}\nCan you guess it?")
    time.sleep(2)
    os.system('cls')
    while guessing_status == True:
        printGuessMap(guessMap)
        user_input = input('Guess: ')

        
        if user_input == 'q':
                print(f"the answer was {answer}, goodbye")
                guessing_status = False
                run = False
                time.sleep(.75)
                os.system('cls')
        elif user_input.isdigit() == False:
            print("enter a number silly goose")
        else:
            user_input = round(int(user_input))
            
            if user_input == answer:
                print("you got it!!!")
                time.sleep(4)
                os.system('cls')
                guessing_status = False

                
            else: 
                if user_input > upper_bound or user_input < lower_bound:
                    print('bruh thats not even in the bounds')
                elif user_input > answer:
                    print("too high!")
                    guessMapUpdate(guessMap,int(user_input))
                else:
                    print("too low!")
                    guessMapUpdate(guessMap,int(user_input))
            
        time.sleep(.75)
        os.system('cls')






