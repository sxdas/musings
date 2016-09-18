# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:49:01 2016

@author: sayooj
"""

epsilon = 0.01
y = 24.0
guess = y/2.0
numguess = 0

while abs(guess*guess-y) >= epsilon:
    numguess += 1
    guess = guess-(((guess**2)-y)/(2*guess))
    print ('guess number: ' + str(numguess) + '; guess: ' + str(guess))
print ('num of guesses = ' + str(numguess))
print('Square root of ' + str(y) + ' is about ' + str(guess))