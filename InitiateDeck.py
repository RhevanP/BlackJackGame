# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:13:25 2020

@author: antho
"""

#Initiate the deck of play
def InitiateDeck(numberxForm,numberOfDecks = 6) :
    return numberxForm * numberOfDecks

#Give te first initiation of the creation
def FirstInitiation() :
    #Create 1 deck
    number = list(range(1,14))
    form = ['Spade', 'Heart', 'Diamond', 'Club']
    numberxForm = []
    for i in number:
        for j in form:
            numberxForm.append(str(i)+' '+j)
    return numberxForm
    