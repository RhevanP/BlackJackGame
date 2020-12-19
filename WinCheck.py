# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:25:40 2020

@author: antho
"""
def WinningCheck(sumCardDraw = 0, sumDealerCardDraw = 0, WinningState = 0):
    #Classic end of the game, we need to check points
    if (WinningState == 0) :
        print("You have", sumCardDraw ,"points")
        print("The Dealer has", sumDealerCardDraw, "points")
        if(sumCardDraw > sumDealerCardDraw) :
            print("You won!")
        elif(sumCardDraw == sumDealerCardDraw) :
            print('It is a tie!')
        else :
            print("You lost...")
    #User has more than 21
    elif (WinningState == 1) :
        print("You drew more than 21, you loose...")
    #Dealer has more than 21
    elif (WinningState == 2) :
        print("The Dealer has more than 21, you Win!")