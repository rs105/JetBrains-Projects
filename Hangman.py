# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:20:15 2020

@author: Romit
"""

import random


chosen = list(random.choice(['java']))
hidden = list('-' * len(chosen))
already_typed = []
print('H A N G M A N')

while input('Type "play" to play the game, "exit" to quit:') != "play":
    continue

count = 0
while count < 8:
    print()
    print("".join(hidden))
    if hidden == chosen:
        print("You guessed the word {}!\nYou survived!".format(''.join(chosen)))
        break
    else:
        
        guess = input('Input a letter: ')
    
        if len(guess) != 1:
            print("You should input a single letter")
            count == count
            
        elif guess in already_typed:
            print('You already typed this letter')
            count == count
  
        elif not guess.islower() or not guess.isalpha():
            print("It is not an ASCII lowercase letter")
            count == count
    
            
       
            
        elif guess not in chosen:
            print('No such letter in the word')
            count += 1
        
        
        elif guess in chosen:
           for i in range(len(chosen)):
               if chosen[i] == guess:
                   hidden[i] = guess
                  
        already_typed.append(guess)
        
if count == 8:
    print("You are hanged!")
                
    
        
