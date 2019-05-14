# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:13:41 2019

@author: shb59
"""
from random import *
def makelotto():
    lotto=[]
    lottoset=set()
    while(len(lottoset)<6):
        lottoset.add(randint(1,10))
    return(list(lottoset))
    
print(makelotto())
