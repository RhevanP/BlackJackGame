# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:59:30 2020

@author: antho
"""
import random

#Draw a card randomly and delete it from the list while returning the card to the user
def DrawCard(deckFinal) :
    #Draw the card
    x = random.choice(deckFinal)
#    print(x)
#    print(deckFinal.index(x))
    #Delete the card from the deck
    deckFinal.pop(deckFinal.index(x))
    #Return the new deck and the value of the card of the user
    return [deckFinal, x]

#Delete the card at the start of the game
def Kickoutcard(deckFinal, destroy = 60) :
    for i in range(1,destroy) :
        x = random.choice(deckFinal)
        deckFinal.pop(deckFinal.index(x))
    return deckFinal