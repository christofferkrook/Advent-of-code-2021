# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:36:28 2021

@author: chk
"""

import os
import numpy as np

def main():
    # part 1
    os.chdir('C:/Users/chk/Documents/GitHub/Advent-of-code-2021/Advent-of-code-2021/Day8')
    f = open("input.txt")
    lines = f.readlines()
    # part 1
    nr = 0
    for line in lines:
        temp = str.split(line, ' | ')
        output = str.split(temp[1], ' ')
        for x in output:
            t = str.split(x, '\n')
            y = len(t[0])
            if y == 2 or y == 4 or y == 7 or y == 3:
                nr += 1
    print(nr)
    
    summation = 0
    # part 2
    for line in lines:
        signals = ['', '', '', '', '', '', '', '', '', '']
        input = str.split(line, ' | ')
        inputs = str.split(input[0], ' ')
        #leng = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for x in inputs:
            y = len(x)
            if y == 2:
                signals[1] = x
            elif y == 3:
                signals[7] = x
            elif y == 4:
                signals[4] = x
            elif y == 7:
                signals[8] = x
        seven = set(sorted(signals[7]))
        eight = set(sorted(signals[8]))
        one = set(sorted(signals[1]))
        four = set(sorted(signals[4]))
        #a = ''.join(seven.symmetric_difference(one))
        fives = [x for x in inputs if len(x) == 5]
        sixes = [x for x in inputs if len(x) == 6]
        
        i = 0
        unused = []
        while i < 3:
            temp = sixes[i]
            temp2 = sixes[i]
            for x in signals[4]:
                temp = temp.replace(x, "")
            for x in signals[1]:
                temp2 = temp2.replace(x, "")
            if len(temp) == 2:
                nine = set(sorted(sixes[i]))
                signals[9] = sixes[i]
                i+=1
                continue
            elif len(temp2) == 4:
                zero = set(sorted(sixes[i]))
                signals[0] = sixes[i]
                i += 1
                continue
            else:
                unused = sixes[i]
                i += 1
        
        #signals[6] = sixes[0]
        signals[6] = unused
        six = set(sorted(signals[6]))
                
        
        i = 0
        while i < 3:
            temp = signals[6]
            temp2 = fives[i]
            for x in fives[i]:
                temp = temp.replace(x, '')
            for x in signals[1]:
                temp2 = temp2.replace(x, '')
            if len(temp) == 1:
                signals[5] = fives[i]
                five = set(sorted(signals[5]))
                i += 1
            elif len(temp2) == 3:
                signals[3] = fives[i]
                three = set(sorted(signals[3]))
                i += 1
            else:
                unused = fives[i]
                i += 1
        signals[2] = unused
        two = set(sorted(signals[2]))
        
        number = ''
        for x in str.split(input[1], ' '):
           temp = str.split(x, '\n')
           inp = temp[0]
           for j in range(len(signals)):
               if len(''.join(set(sorted(inp)).symmetric_difference(set(sorted(signals[j]))))) == 0:
                   number = number + str(j)
                   continue
        
        summation += int(number)
    print(summation)
        
if __name__ == '__main__':
    main()