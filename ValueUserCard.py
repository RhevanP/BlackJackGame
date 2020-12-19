# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:16:05 2020

@author: antho
"""

#Create the switcher
def name(x) :
    switcher={
            1 : 'Ace',
            11 : 'Jack',
            12 : 'Queen',
            13 : 'King'
            }
    return switcher.get(x,'critical error occured')

#manage the list of card drawn and store the value of each card
def ValueUserCard(x, jackSup = 10):
    numberDetected = int(''.join(map(str,list(filter(str.isdigit, x)))))
    #When Jack or superior
    if numberDetected > jackSup:
        #Name of the card
        cardName = name(numberDetected) + ' of' +''.join([i for i in x if not i.isdigit()])
        #Value of the card
        cardValue = jackSup
    elif numberDetected == 1 : #When ace, which means that it can be eleven or 1.
        cardName = name(numberDetected) + ' of' +''.join([i for i in x if not i.isdigit()])
        cardValue = 11
    else : #when 2 to 10
        #Name of the card
        cardName = x
        #Value of the card
        cardValue = numberDetected
    #print for check
#    print(cardName)
#    print(cardValue)
    #return the lists of value and drawing names
    return [cardName, cardValue]