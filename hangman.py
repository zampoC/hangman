# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:50:49 2019

@author: zampochung
"""

"""Hangman"""


def hangman(word):
    wrong = 0
    stages = ["",
              "|__________           ",
              "|                     ",
              "|          |          ",
              "|          0          ",
              "|        / | \        ",
              "|         / \         ",
              "|                     "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to the Russian rounds Geame!!!!")
    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] =char
            rletters[cind] ='$'
        else:
            wrong +=1  
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))   
        if "_" not in board:
            print("You Win")
            print(" ".join(board))
            win = True
            break            
    if not win:
            print("\n".join(stages[0: wrong]))
            print("You lose! It was {}".format(word))
        

def ran_list():
    import csv
    with open("E:\Python Learning\list.csv", "r") as f:
        r = csv.reader(f)        
        list_csv=[]
        for row in r:
            list_csv.append(row)
    import random
    j = random.randint(0, len(list_csv)-1)
    tran_str = list_csv[j]  
    hangman(tran_str[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        