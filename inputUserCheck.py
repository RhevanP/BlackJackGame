# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:38:08 2020

@author: antho
"""

def inputUserCheck(drawUserValue) :
    if (len(drawUserValue) > 1) : 
        while True :
            userInput = input('Do you want to Draw (1) or Stop (2) ?')
            try :
                userInput = int(userInput)
                if userInput != 2 and userInput != 1 :
                    print("You did not enter a valid number, it's either 0 or 1!")
                else :
                    break
            except :
                userInputLowered = userInput.lower()
                if userInputLowered == 'draw' or userInputLowered == 'd' :
                    userInput = 1
                    print('drawing')
                    break
                elif userInputLowered == 'stop' or userInputLowered == 's' :
                    userInput = 2
                    print('stopping')
                    break
                else :
                    print('you did not input a correct option')
    else :
        userInput = 1
        print('Drawing...')
    return userInput