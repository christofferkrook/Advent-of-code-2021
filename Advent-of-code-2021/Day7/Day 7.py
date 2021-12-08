# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 07:30:59 2021

@author: chk
"""

import os
import numpy as np

def main():
    # part 1
    os.chdir('C:/Users/chk/Documents/GitHub/Advent-of-code-2021/Advent-of-code-2021/Day7')
    f = open("input.txt")
    positions = str.split(f.readline(), ',')
    
    for i in range(len(positions)):
        positions[i] = int(positions[i])
    
    smallestFuelPos = np.round(np.median(positions))
    
    fuel = 0
    for x in positions:
        fuel += np.abs(smallestFuelPos - x)
    
    print(int(fuel))
    
    
    # part 2
    
    smallestFuelPos = np.round(sum(positions)/len(positions))
    
    temp = 0
    for x in positions:
        temp += (sum(list(range(1, int(np.abs(x-smallestFuelPos)) + 1))))

    print(temp)
   
    
if __name__ == '__main__':
    main()