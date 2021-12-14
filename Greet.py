"""
***************************************************************************
Filename: Greet.py
Author: Nathaniel
Date: 2021.10.28
Modifications: Nathaniel - 2021.12.13
Description: A program that greets you and has some functions
             like playing a game or centering text
             Function Includes:
1) greeting(): Greets you and prompts you for why game you want to play. 
2) guessing(): Guessing number game.
3) center()  : Center text 
***************************************************************************
"""

### Modules Import Here ###
from os import terminal_size
import random as rand


#################################
###### Function Start Here ######
#################################

def greeting():
    """
    ************************************************************************
    Function     : greeting()
    Inputs       : 1.) Takes your name
                   2.) Choice for either a game or centering text
    Outputs      : 1.) Return your name
                   2.) Redirects you to either function guessing() or center()
    Returns      : None
    Author       : Nathaniel
    Date         : 2021.12.13
    Description  :
    1.) Take name and greet you
    2.) Ask what you want to do
    ************************************************************************
    """

    name = input("Welcome to this program! What's your name? ")
    print("Hi,", name)
    
    choice = input("What would you like to do today? Type game to play a game and center to center some characters, Q to quit. ")
    while choice != "q" or choice != "Q":
        choice = choice.lower()  
        if choice == "game":
            guessing()
            choice = input("\nWhat would you like to do today? Type game to play a game and center to center some characters, Q to quit. ")
        elif choice == "center":
            center()
            choice = input("\nWhat would you like to do today? Type game to play a game and center to center some characters, Q to quit. ")
        elif choice == "Q" or choice == "q":
            print("Bye!")
            exit()
        else:
            choice = input("\nError, What would you like to do today? Type game to play a game and center to center some characters, Q to quit. ")

def guessing():
    """
    ************************************************************************
    Function     : guessing()
    Inputs       : 1.) Takes a number
    Outputs      : 3 outputs, Either (Too Small), (Too Big), and (Correct!)
    Returns      : None
    Author       : Nathaniel
    Date         : 2021.12.13
    Description  :
    1.) Play's a lame guessing game i made in <5 mins
    ************************************************************************
    """
    randomnum = rand.randint(0,100)
    number = eval(input("Guess a number from 0-100: "))
    while not(number == randomnum):    
        if number <= randomnum:
            print("Too Small")
            number = eval(input("Guess a number from 0-100: "))
        elif number >= randomnum:
            print("Too Big")
            number = eval(input("Guess a number from 0-100: "))
        else:
            print("Correct!")

def center():
    """
    ************************************************************************
    Function     : center()
    Inputs       : 1.) Takes text
    Outputs      : Centered text
    Returns      : None
    Author       : Nathaniel
    Date         : 2021.12.13
    Description  :
    1.) Os module to get terminal size so coder doesn't have to center space
    ************************************************************************
    """
    import os
    
    termimalsize = os.get_terminal_size().columns

    text = input("Center some text: ")
    multiple = 0

    for i in text:
        multiple += 1
        
    spaces = " " * int(round(((termimalsize - multiple)/2)))

    print(spaces, text, spaces)

#End of Functions




"""
********************************************************************************
                            PROGRAM STARTS HERE

Description:
1.) Calls on the greeting() function
    - The greeting() function will call on the other 2 function
********************************************************************************
"""

greeting()





    