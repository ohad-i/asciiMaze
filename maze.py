# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:38:24 2015

@author: meni_s, ohad-i
"""

#import os
#os.system("start notepad.exe")

import numpy as np
import random
import sys

realTimePrint = False

def createMaze(size, wall = '*', space = ' '):
    
    maze= np.zeros((size,size),np.byte) #[[0 for j in range(size)] for i in range(size)]
    resMaze = ''
    #Building maze around path
    i = 0
    
    while (i < size):
        j = 0
        while (j < size):
            if (i==0)or(i==size-1): maze[i][j] = 1
            if (j==0)or(j==size-1): maze[i][j] = 2
            j = j + 1
        i = i + 1
        
    #print maze
    
    #Creating path
    
    i = random.randint(1,size-2)
    j = 0
    move=0
    prevMove = move
    maze[i][j] = 4
    j = 1;
    vertMove=0
    
    while (j < size):
        if (i==0): i=1
        if (i==size-1): i=size-2
        maze[i][j] = 4    
        move = random.randint(1,3)
        if (j==size-1): move=2
        if (move==1)and(prevMove != 3):        
            i = i-1
            prevMove = move        
            vertMove=0
        if (move==2): 
            j = j+1
            vertMove=vertMove+1
            if (vertMove==2):
                prevMove = 0
                vertMove = 0            
        if (move==3)and(prevMove != 1):
            prevMove = move
            i = i+1
            vertMove=0
                    
        #print "move: ", move, " prevMove: ", prevMove, " vertMove: ", vertMove, " j: ", j
    
    #Completing maze
    i=0
    j=0
    cell=0
    while (i < size):
        j=0    
        while (j < size):     
            cell = random.randint(0,3)
            if (maze[i][j]==0):
                maze[i][j]=cell
            j=j+1
            #print "i: ",i," j:",j," cell: ",cell
        i=i+1
        
        
    #Print maze    
    i=0
    j=0
    cell=0
    
    for i in range(size):
        for j in range(size):
            if (maze[i][j]==0): 
                curVal = space
            if (maze[i][j]==1): 
                curVal = wall
            if (maze[i][j]==2): 
                curVal = wall
            if (maze[i][j]==3): 
                curVal = space
            if (maze[i][j]==4): 
                curVal = space
            if realTimePrint:
                print(curVal[0],)
            resMaze += curVal[0]
            
        resMaze += '\n'
        if realTimePrint:
            print("\n",)
    return resMaze 


'''
Activation: to get 20x20 maze:
python maze.py 20
by default, 15x15
'''
     
if __name__=="__main__":
    if len(sys.argv) > 0:
        size = int(sys.argv[1])
    else:
        size = 15
    
    maze = createMaze(size)

    print('-'*size)
    print(maze)
