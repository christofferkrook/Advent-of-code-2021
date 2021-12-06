# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:42:37 2021

@author: chk
"""

import os
import numpy as np

def main():
    # part 1
    os.chdir('C:/Users/chk/Documents/GitHub/Advent-of-code-2021/Advent-of-code-2021/Day6')
    f = open("input6.txt")
    
    ages = f.readline()
    ages = str.split(ages, ',')

    
    # part 2
    
    fishes = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype='int64')
    
    for x in ages: 
        fishes[int(x) +1] += 1
        
    newfish = 0
    for i in range(256):
        if np.mod(i, 10) == 0:
            print("")
        fishes = np.roll(fishes, -1)
        fishes[7] = fishes[7] + fishes[0]
        fishes [9] = fishes[0]
        fishes[0] = 0
        print(i)
    print(sum(fishes))
        
    
if __name__ == '__main__':
    main()