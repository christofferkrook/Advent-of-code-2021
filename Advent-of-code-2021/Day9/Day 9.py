# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:36:28 2021

@author: chk
"""

import os
import numpy as np

def main():
    # part 1
    os.chdir('C:/Users/chk/Documents/GitHub/Advent-of-code-2021/Advent-of-code-2021/Day9')
    f = open("input.txt")
    lines = f.readlines()
    # part 1
    
    grid = np.zeros((100, 100))

    y = 0
    x = 0

    for line in lines:
        x = 0
        for t in line:
            if not(t == '\n'):
                grid[y][x] = t
                x += 1
        y += 1
        
    risk = 0
    
    for i in range(100):
        for j in range(100):
            val = int(grid[i][j])
            if i == 0:
                if j == 0:
                    if val < int(grid[i][j+1]) and val < int(grid[i+1][j]):
                        risk += 1+val
                elif j == 99:
                    if val < int(grid[i][j-1]) and val < int(grid[i+1][j]):
                        risk += 1+val
                else:
                    if val < int(grid[i][j-1]) and val < int(grid[i+1][j]) and val < int(grid[i][j+1]):
                        risk += 1+val  
            elif i == 99:
                if j == 0:
                    if val < int(grid[i-1][j]) and val < int(grid[i][j+1]):
                        risk += 1+val
                elif j == 99:
                    if val < int(grid[i-1][j]) and val < int(grid[i][j-1]):
                        risk += 1+val
                else:
                    if val < int(grid[i][j-1]) and val < int(grid[i-1][j]) and val < int(grid[i][j+1]):
                        risk += 1+val
            elif j == 0 and not(i == 0):
                if val < int(grid[i-1][j]) and val < int(grid[i][j+1]) and val < int(grid[i+1][j]):
                    risk += 1+val
            elif j == 99 and not(i == 0):
                if val < int(grid[i-1][j]) and val < int(grid[i][j-1]) and val < int(grid[i+1][j]):
                    risk += 1+val
            else:
                if val < int(grid[i-1][j]) and val < int(grid[i+1][j]) and val < int(grid[i][j-1]) and val < int(grid[i][j+1]):
                    risk += 1+val
        print(risk)
if __name__ == '__main__':
    main()