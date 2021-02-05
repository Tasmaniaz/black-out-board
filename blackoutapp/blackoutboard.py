# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:21:53 2020

@author: Janni
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.currentPos = 0

player1n = Player("Jannic")
player2n = Player("Rene")
player3n = Player("Tobias")
player4n = Player("Ich Heis Heise")
player5n = Player("Ninn")
player6n = Player("Baldy")

players = [player1n, player2n, player3n, player4n, player5n, player6n]

currentPlayer = players[0]
currentPlayerTurn = 0
        

def fields():
    if (player==1):
        print(name + " finnish your drink")
    elif (player==2):
        print(name +" person to the left drinks!")
    elif (player==3):    
        print(name + " rock paper scissors with random peron, loser drinks")
    elif (player==4):
        print(name +" flip a coin: heads - take a shot, tails - your're safe")
    elif (player==5):
        print(name + " guys drink")
    elif (player==6):
        print(name + " 5 push ups")
    elif (player==7):
        print(name + " sniper counting")
    elif (player==8):
        print(name +" take a ship from the person to your right AND left")
    elif (player==9):    
        print(name + " never have I ever...")
    elif (player==10):
        print(name +" pick a drinking buddy")
    elif (player==11):
        print(name + " take a shot")
    elif (player==12):
        print(name + " ladies drink")
    elif (player==13):
        print(name + " tell an embarrassing story about yourself")
    elif (player==14):
        print(name +" mute untill its your turn again")
    elif (player==15):    
        print(name + " Hmmmm water...")
    elif (player==16):
        print(name +" shot or dare")
    elif (player==17):
        print(name + " categories")
    elif (player==18):
        print(name + " spin the bottle, person it lands on, drinks")
    elif (player==19):
        print(name +" bust a rhyme")
    elif (player==20):    
        print(name + " waterfall")
    elif (player==21):
        print(name +" give 5 sips")
    elif (player==22):
        print(name + " you are the Snack King - only people with your allowance is allowed to take from the snacks")
    elif (player==23):
        print(name + " 10 push ups")
    elif (player==24):
        print(name + " social drink")
    elif (player==25):
        print(name +" roll a dice, drink the number it lands on")
    elif (player==26):    
        print(name + " 2 truths 1 lie")
    elif (player==27):
        print(name +" the most sober person takes a shot (common vote)")
    elif (player==28):
        print(name + " tallest drinks")
    elif (player==29):
        print(name + " finnish your drink")
    elif (player==30):
        print(name + " give 1 shot")
    elif (player==31):
        print(name +" pick someone to finnish their drink, and make their new one")
    elif (player==32):    
        print(name + " question master: ask anyone, anything")
    elif (player==33):
        print(name +" youngest drinks")
    elif (player==34):
        print(name + " 10 pushups")
    elif (player==35):
        print(name + " make a rule")  
    elif (player==36):
        print(name + " show the last message u recieved")
    elif (player==37):
        print(name + " shortest drink")
    elif (player==38):
        print(name + " quote The Office or drink")
    elif (player==39):
        print(name +" table-thumb game")
    elif (player==40):    
        print(name + " guys drink")
    elif (player==41):
        print(name +" switch your drink with the person to your left")
    elif (player==42):
        print(name + " do an impression of someone famous, if people cannot guess it you drink 4 sips")
    elif (player==43):
        print(name + " buffalo")
    elif (player==44):
        print(name +" switch places with the third person to your right")
    elif (player==45):    
        print(name + " hum a song, if people cannot guess it, you drink 5 sips")
    elif (player==46):
        print(name +" ladies drinks")
    elif (player==47):
        print(name + " switch shirt with the person to your right")
    elif (player==48):
        print(name + " quote z Disney movie or drink")
    elif (player==49):
        print(name + " take a shot")
    elif (player==50):
        print(name +" make a rule")
    elif (player==51):    
        print(name + " make an impression of a player, whoever guesses can give 5 sips")
    elif (player==52):
        print(name +" bust a rhyme")
    elif (player==53):
        print(name + " finnish your drink")
    elif (player==54):
        print(name + " is finnished")
    elif (player==55):
        print(name + " is finnished")
    elif (player==56):
        print(name +" is finnished")
    elif (player==57):    
        print(name + " is finnished")
    elif (player==58):
        print(name +" is finnished")
    elif (player==59):
        print(name + " is finnished")
    elif (player==60):
        print(name + " you are finished now please stop playing")
    
while 1 == 1:
    dice =  random.choice(range(1,6))
    currentPlayer.currentPos += dice
    name = currentPlayer.name
    print(name + " rolled " + str(dice))
    print("Current board position: " + str(currentPlayer.currentPos))
    
    player = currentPlayer.currentPos
    fields()
    
    if (currentPlayerTurn == len(players) - 1):
        currentPlayerTurn = 0
    else:
        currentPlayerTurn += 1
    
    currentPlayer = players[currentPlayerTurn]
    
    next_turn = input('Next player ready?')
    
    if next_turn == 'yes' or next_turn == 'y':
        again = True
    else:
        again = False