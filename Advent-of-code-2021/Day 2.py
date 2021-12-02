# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:05:54 2021

@author: chk
"""
import os
def main():
    os.chdir('C:/Users/chk/Documents/GitHub/Advent-of-code-2021/Advent-of-code-2021')
    f = open("input.txt.txt")
    
    lines = f.readlines()
    
    
    # part 1
    x = 0
    y = 0
    
    for i in range(len(lines)):
        a = str.split(lines[i], ' ')
        if a[0] == 'forward':
            x += int(a[1])
        elif a[0] == 'backwards':
            x -= int(a[1])
        elif a[0] == 'up':
            y -= int(a[1])
        elif a[0] == 'down':
            y += int(a[1])
    print('Part 1: Product of positions is ' + str(x*y))
    
    # part 2
    x = 0
    y = 0
    aim = 0
    
    for i in range(len(lines)):
        a = str.split(lines[i], ' ')
        if a[0] == 'forward':
            x += int(a[1])
            y = y + aim*int(a[1])
        elif a[0] == 'backwards':
            x -= int(a[1])
        elif a[0] == 'up':
            #y -= int(a[1])
            aim -= int(a[1])
        elif a[0] == 'down':
            #y += int(a[1])
            aim += int(a[1])
    
    print('Part 2: Product of positions is ' + str(x*y))
    
if __name__ == '__main__':
    main()