# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:27:50 2020

@author: antho
"""

import InitiateDeck as ID
import DrawCard as DC
import ValueUserCard as VUC
import inputUserCheck as IUC
import WinCheck as WC
import Aces
import Players

Player = Players.Gambler(1,1)
Dealer = Players.Gambler(1,1)
#Composition of 1 deck
numberxForm = ID.FirstInitiation()
#list of what you drew
blackJackValue = 21
aceValue = 11
aceValue2 = 1
drawInputUser = 1
stopInputUser = 2
winningState = 0
#Create 6 decks
deckFinal = ID.InitiateDeck(numberxForm)
#Delete 70cards of it
##deckFinal = DC.Kickoutcard(deckFinal)


def DrawingCard(deckFinal, drawUser, drawUserValue, secret = 0) :
    #Take a card randomly from the deck
        result = DC.DrawCard(deckFinal)
        x = result[1]
        deckFinal = result[0]
        #Detect the name (drawUser) and the value of the card (drawUserValue)
        valueUserCardResult = VUC.ValueUserCard(x)
        drawUser.append(valueUserCardResult[0])
        drawUserValue.append(valueUserCardResult[1])
        #Variable to exit the loop at blackJackValue+
        sumCardDraw = sum(drawUserValue)
        #Printing the draw of the user (list), the draw of the user value (List) and the Sumofcard
        #Hiding the draw for the first 2 draws from the dealer
        if(secret == 1 and len(drawUser) == 2):
            print("The Dealer Drew his second card... It's hidden for now")
        else :
            print(drawUser)
            print(sumCardDraw)
        return [deckFinal, drawUser, drawUserValue, sumCardDraw]

def DealerDrawing(deckFinal, drawDealer, sumDealerCardDraw, drawDealerValue) :
    #Reveal
    print ("Here's the hand of the Dealer !")
    print(drawDealer)
    print(sumDealerCardDraw)
        #Dealer double ace or blackjack?
    if(sumDealerCardDraw >= blackJackValue) :
        if(sumDealerCardDraw == blackJackValue+1 ) :
            [drawDealerValue, sumDealerCardDraw] = Aces.DearlerSavedByAce(drawDealerValue, aceValue, aceValue2, sumDealerCardDraw, drawDealer)
        else :
            print('The Dealer did a natural blackjack... Oopsie')
    #While
    while sumDealerCardDraw < 17 :
        print("Dealer Drawing")
        [deckFinal, drawDealer, drawDealerValue, sumDealerCardDraw] = DrawingCard(deckFinal, drawDealer, drawDealerValue)
    #Conclusion
    if sumDealerCardDraw > 21 :
        print('The Dealer drew', sumDealerCardDraw, 'which is more than the blackjack and lost')
        return [deckFinal, drawDealer,sumDealerCardDraw,drawDealerValue,2]
    else :
        print("Dealer has finished drawing and has", sumDealerCardDraw, "points")
        return [deckFinal, drawDealer,sumDealerCardDraw,drawDealerValue,0]

while True :
    nCardDraw = len(Player.drawUserValue)
    while nCardDraw < 1:
        nCardDraw = len(Player.drawUserValue)
        ##UserDrawing
        print('Dealing the User the ', nCardDraw + 1, ' Card')
        [deckFinal, Player.drawUser, Player.drawUserValue, Player.sumCardDraw] = DrawingCard(deckFinal, Player.drawUser, Player.drawUserValue)
        #user double ace or blackjack?
        if(Player.sumCardDraw >= blackJackValue) :
            if(Player.sumCardDraw == blackJackValue+1) :
                [Player.drawUserValue, Player.sumCardDraw] = Aces.SavedByAce(Player.drawUserValue, aceValue, aceValue2, Player.sumCardDraw, Player.drawUser)
                nCardDraw = len(Player.drawUserValue)
            else :
                print('You did a natural blackjack it is beautiful!')
        ###DealerDrawing
        print("Drawing Dealer the", nCardDraw + 1, " Card")
        [deckFinal, Dealer.drawUser, Dealer.drawUserValue, Dealer.sumCardDraw] = DrawingCard(deckFinal, Dealer.drawUser, Dealer.drawUserValue, 1)
        #Did we finish to draw 2 cards ?
        if(nCardDraw == 1) :
            if(Dealer.sumCardDraw == 21) :
                print('The dealer did a natural blackjack')
                print(Dealer.drawUser)
                print(Dealer.sumCardDraw)
            print('Finishing to draw the initial cards...')
            break
        
    #Checking if SumCardDraw is blackjack value (21) and drew 2 cards (1) yet
    if((Player.sumCardDraw ==blackJackValue and nCardDraw == 2) or (Dealer.sumCardDraw==blackJackValue and nCardDraw ==2)) :
        WC.WinningCheck(Player.sumCardDraw, Dealer.sumCardDraw)
        break
    
    
    #Ask the user to get an input and check it
    inputUser = IUC.inputUserCheck(Player.drawUserValue)
    if inputUser == drawInputUser:
        [deckFinal, Player.drawUser, Player.drawUserValue, Player.sumCardDraw] = DrawingCard(deckFinal, Player.drawUser, Player.drawUserValue)
        #If it's beyond 21 and you drew an ace, you change the value of the ace
        if Player.sumCardDraw > blackJackValue and aceValue in Player.drawUserValue:
            [Player.drawUserValue, Player.sumCardDraw] = Aces.SavedByAce(Player.drawUserValue, aceValue, aceValue2, Player.sumCardDraw, Player.drawUser)
        #If it's blackjack
        elif Player.sumCardDraw == blackJackValue :
            print('BLACKJACK BABY!')
            ########WHAT IF DEALER CAN HAVE BLACKJACK AS WELL?
            break
        #If it's more than blackjack
        elif Player.sumCardDraw > blackJackValue :
            WC.WinningCheck(WinningState =  1)
            break
    else :
        print('You Stopped the Draw')
        if (Dealer.sumCardDraw == 21) :
            WC.WinningCheck(Player.sumCardDraw, Dealer.sumCardDraw, winningState)
        else :
            [deckFinal, Dealer.drawUser, Dealer.sumCardDraw, Dealer.drawUserValue, winningState] = DealerDrawing(deckFinal, Dealer.drawUser, Dealer.sumCardDraw, Dealer.drawUserValue)
            WC.WinningCheck(Player.sumCardDraw, Dealer.sumCardDraw, winningState)
        break


###TO DO :
#Add the system of "Bid"
#if a player has a natural Blackjack and the Dealer doesn't, the Dealer pay 1.5x times the amount of the best
#If there's two card with same denomination (2 jacks, 2 sixes, etc...), player can play "Twice" by divind his game in 2
    #With a pair of aces, the player is given one card for each ace and may not draw again.
        #Also, if a ten-card is dealt to one of these aces, the payoff is equal to the bet (not one and one-half to one, as with a blackjack at any other time).
#Another option open to the player is doubling their bet when the original two cards dealt total 9, 10, or 11. !!DOUBLE 5 EXCEPTION!!
#Reshuffling : only reshuffling after a game if it goes to a certain amount of card drawn in total.

