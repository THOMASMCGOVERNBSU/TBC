#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:52:03 2024

@author: thomasmcgovern
"""

import random
class Character(object):
    def __init__(self, name= "Hero", HP= 20, hitChance = 50, maxDamage= 3, armor= 1):
        super().__init__()
        self.name= name
        self.HP = HP
        self.hitChance= hitChance
        self.armor = armor
        
        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self, value):
            self.__name= value
        
        @property
        def HP(self):
            return self.__HP
        @HP.setter
        def HP(self, value):
            self.__HP= value
        
        @property
        def hitChance(self):
            return self.__hitChance
        @hitChance.setter
        def hitChance(self, value):
            self.__hitChance= value
            
        @property
        def maxDamage(self):
            return self.__maxDamage
        
        @maxDamage.setter
        def maxDamage(self, value):
            self.__maxDamage= value
        
        @property
        def armor(self):
            return self.__armor
        @armor.setter
        def armor(self, value):
            self.__armore= value
            
def stats(self):
            print(f"""
        {self.name}
        HP: {self.HP}
        Hit Chance: {self.hitChance}
        Max Damage: {self.maxDamage}
        Armor: {self.armor}
             """)

def fight(self, monster):
    hitOdds = random.randint(0, 100)
    if int(hitOdds) <= 30:
        print(f"{self.name} hit {monster.name}")
        playerDamage = random.randint(0, self.maxDamage)
        finalDamage= int(playerDamage)- int(self.armor)     
        if int(finalDamage) < 0:
            finalDamage = 0 
            if monster.armor > 0:
                print(f"{monster.name}'s armor blocks the attack")
            print(f"You still hit the monster for {finalDamage} points of damage")
        monster.HP -= finalDamage
    else: 
        print(f"{self.name} misses {monster.name}")
        
def main(hero, monster):
    hero = Character()
    hero.name = "Hero"
    monster = Character()
    monster.name = "Monster"
    
    hero.stats()
    monster.stats()
   

if __name__== "__main__":
    main("hero", "monster")
    
            