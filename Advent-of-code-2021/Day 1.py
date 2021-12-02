# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:05:54 2021

@author: chk
"""
import os
def main():
    os.chdir('C:/Users/chk/Advent of code day 1')
    f = open("input.txt")
    
    lines = f.readlines()
    
    # part 1
    larger = 0
    for i in range(len(lines)):
        if i > 0:
            if int(lines[i]) > int(lines[i-1]):
                larger +=1
    print(larger)
    
    
    # part 2
    larger = 0
    temp = int(lines[0]) + int(lines[1]) + int(lines[2])
    for i in range(len(lines)):
        if i > 2:
            if (int(lines[i]) + int(lines[i-1]) + int(lines[i-2])) > temp:
                larger += 1
            temp = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
    print(larger)
    
if __name__ == '__main__':
    main()