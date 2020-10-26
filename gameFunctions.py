# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:51:57 2020

@author: Quang Anh Nguyen
"""


def input_collector():
    return input("> ")
        
def choice_checker(choice, is_InCorrect):
    while (is_InCorrect):
        choice = choice.upper()
        if (choice == "Y"  or choice == "N"):
            is_InCorrect = False
        else:
            print("Your choice is invalid. PLEASE enter a different choice")
            choice = input_collector()
    return choice    
       
def guess_checker(guess, is_InCorrect):
    while (is_InCorrect):
        guess = int(guess)
        if (guess < 0 or guess > 20):
            print("Your guess is invalid. PLEASE enter another guess")
            guess = input_collector()
        else:
            is_InCorrect = False
    return guess
                
