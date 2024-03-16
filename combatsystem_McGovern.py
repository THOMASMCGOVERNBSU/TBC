#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:21:07 2024

@author: thomasmcgovern
"""

import tbc

def main():
        keepGoing = True
        hero = tbc.Character()
        hero.name= "Player"
        hero.HP = 10
        hero.hitChance= 50
        hero.maxDamage = 5
        hero.armor = 2 
        
        monster = tbc.Character("Monster", 20, 30, 5, 0)
        monster = tbc.Character
        monster.name = "Monster"
        monster.HP = 20
        monster.hitChance= 30
        monster.maxDamage = 5
        monster.armor = 0
        
        tbc.stats(hero)
        tbc.stats(monster)
    
        while keepGoing == True:
        
            tbc.fight(hero, monster)
            tbc.fight(monster, hero)
            tbc.stats(monster)
            tbc.stats(hero)
            
            if hero.HP <= 0:
                print("You have been defeated by the monster. Game over.")
                keepGoing = False
            elif monster.HP <= 0:
                print("Congratulations! You have defeated the monster.")
                keepGoing = False


    
if __name__ == "__main__":
    main()
    keepGoing= True
    
    while keepGoing == True:
        
        choice = input("Do you want to 'restart' the game or 'quit'? ").lower()
        if choice == 'restart':
            main()
        elif choice == 'quit':
            print("Thank you for playing. Goodbye!")
            keepGoing= False 