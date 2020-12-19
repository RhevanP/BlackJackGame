# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:08:27 2020

@author: antho
"""
def SavedByAce(drawUserValue, aceValue, aceValue2, sumCardDraw, drawUser) :
    drawUserValue[drawUserValue.index(aceValue)] = aceValue2
    sumCardDraw -= (aceValue - aceValue2)
    print('You have been saved by your ace!')
    print(drawUser)
    print(sumCardDraw)
    return [drawUserValue, sumCardDraw]


def DearlerSavedByAce(drawUserValue, aceValue, aceValue2, sumCardDraw, drawUser) :
    drawUserValue[drawUserValue.index(aceValue)] = aceValue2
    sumCardDraw -= (aceValue - aceValue2)
    print('Dealer has been saved by his ace!')
    print(drawUser)
    print(sumCardDraw)
    return [drawUserValue, sumCardDraw]

drawUserValue = [11,11]