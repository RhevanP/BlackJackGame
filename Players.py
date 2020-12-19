# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:36:36 2020

@author: antho
"""
class Gambler :
    
    
    def __init__(self, bidValue, moneyTot) :
        self.bidValue = bidValue
        self.moneyTot = moneyTot
        self.drawUser = []
        self.drawUserValue = []
        self.sumCardDraw = 0