# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import simpleaudio as sa

from random import randint

def playgame():

    #create a list of play options
    t = ["Rock", "Paper", "Scissors"]

    #assign a random play to the computer
    computer = t[randint(0,2)]
    
        #set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
            print("Tie!")
    elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
                    cheer()
    elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
                    cheer()
    elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
                    cheer()
    else:
            print("That's not a valid play. Check your spelling!")
            #player was set to True, but we want it to be False so the loop continues
    
    
    print(computer)
    


def cheer():
    filename = 'KidsCheering.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing)
    
def main():
    print("in main")
    while True:
        playgame()
        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break
            

if __name__ == "__main__":
	main()          
            
            