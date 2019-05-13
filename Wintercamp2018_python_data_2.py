# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:56:34 2019

@author: shb59
"""

from random import randint

def makelotto():
    signal=0
    i=0
    lotto=[]
    
    while(1):
        temp=randint(1,10)
        if(temp not in lotto):
            lotto.append(temp)
        if(len(lotto)==6):
            break
            
    return lotto

print(makelotto())
