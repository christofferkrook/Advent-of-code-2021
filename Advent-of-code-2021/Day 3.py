# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:56:46 2021

@author: chk
"""


import os
def main():
    os.chdir('C:/Users/chk/Documents/GitHub/Advent-of-code-2021/Advent-of-code-2021')
    f = open("input3.txt")
    
    lines = f.readlines()


# part 1
    A = [0, 0, 0, 0, 0]    
    B = [0, 0, 0, 0, 0]    
    #A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    N = len(lines)
    
    for line in lines:
      for i in range(len(A)):
          A[i] = A[i] + int(line[i])
          
    for i in range(len(A)):
        if int(A[i]) > N/2:
            A[i] = 1
            B[i] = 0
        else:
            A[i] = 0
            B[i] = 1
            
    gamma = ''
    beta = ''
    for i in range(len(A)):
        gamma = gamma + str(A[i])
        beta = beta + str(B[i])
    gamma = int(gamma, 2)
    beta = int(beta, 2)
    print('Gamma is ' + str(gamma))
    print('Beta is ' + str(beta))
    print('The power is ' + str(beta*gamma))

    # part 2
    index = 0
    B = lines
    while len(B) > 1:
        temp = 0
        for i in range(len(B)):
            a = str(B[i])
            if int(a[index]) == 1:
                temp += 1
        if temp >= len(B)/2:
            c = 1
        else:
            c = 0
        C = []
        for line in B:
            if int(line[index]) == c :
                C.append(line)
        B = C
        index += 1
        
    index = 0
    D = lines
    while len(D) > 1:
        temp = 0
        for i in range(len(D)):
            a = str(D[i])
            if int(a[index]) == 1:
                temp += 1
        if temp >= len(D)/2:
            c = 0
        else:
            c = 1
        C = []
        for line in D:
            if int(line[index]) == c :
                C.append(line)
        D = C
        index += 1
        
    scrubber = ''
    generator = ''
    generator = int(generator + str(B[0]), 2)
    scrubber = int(scrubber + str(D[0]), 2)

    print('Generator is ' + str(generator))
    print('Scrubber is ' + str(scrubber))
        

    


if __name__ == '__main__':
    main()