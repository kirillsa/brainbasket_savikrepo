# -*- coding: utf-8 -*-
#Savitskiy Kirill
#Problem set 3
#
#Problem 1
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def rediationExposure(start, stop, step):
    sum = 0
    while start<stop:
        sum += f(start)*step
        start += step
    return sum
#
print (rediationExposure(0,5,1))
print (rediationExposure(5,11,1))
print (rediationExposure(0,11,1))
print (rediationExposure(40,100,1.5))
#
#Problem 2
def isWordGuessed(secretWord, lettersGuessed):
    for ch in secretWord:
        if ch not in lettersGuessed:
            return 0
    return 1
#
print (isWordGuessed('apple',['a','p','l','E']))
#
#Problem 3
def getGuessedWord(secretWord,lettersGuessed):
    assert secretWord.islower()
    #assert c for c in lettersGuessed if c.islower()
    str = ''
    for ch in secretWord:
        if ch in lettersGuessed:
            str += ch
        else:
            str += '_ '
    return str
#
print (getGuessedWord('apple',['e','i','k','p','r','s']))
#
#Problem 4
def getAvailableLetters(lettersGuessed):
    str = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for ch in letters:
        if ch not in lettersGuessed:
            str += ch
    return str    
#
print (getAvailableLetters(['e','i','k','p','r','s']))
#
#Problem 5
def hangman(secretWord):
    lettersGuessed = []
    while True:
        guess = ''
        while guess not in 'qwertyuiopasdfghjklzxcvbnm' or len(guess)>1 or guess is '':
            guess = input('Enter 1 character: ')
            guess = guess.lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if isWordGuessed(secretWord, lettersGuessed):
                print (getGuessedWord(secretWord, lettersGuessed))
                print ("You WIN")
                break
            else:
                print (getGuessedWord(secretWord, lettersGuessed))
        else:
            print ('You have entered the letter that you have already entered')
            print ('enter letter that is in this list', getAvailableLetters(lettersGuessed))
            continue
        
#
hangman ("kirill")
