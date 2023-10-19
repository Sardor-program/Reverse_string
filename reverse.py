# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:11:43 2023

@author: hp
"""



def reverseString(text):
    text = list(text)
    for i in range(len(text)//2):
        mirrorIndex = len(text)-1-i
        text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
    return ''.join(text)    
        
        