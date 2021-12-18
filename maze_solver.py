# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:05:37 2015

@author: meni_s, ohad-i
"""

import sys 
import time
import emoji

if len(sys.argv)>1:
    size = int(sys.argv[1])
else:
    size = 10
    
if 0:
    "Create maze"
    # 2 -> wall
    # 0 -> space
    size = 5
    maze=[[0 for j in range(size)] for i in range(size)]
    
    maze[0][0]=2
    maze[0][1]=0
    maze[0][2]=0
    maze[0][3]=0
    maze[0][4]=2
    
    maze[1][0]=2
    maze[1][1]=0
    maze[1][2]=2
    maze[1][3]=0
    maze[1][4]=2
    
    maze[2][0]=0
    maze[2][1]=0
    maze[2][2]=2
    maze[2][3]=2
    maze[2][4]=2
    
    maze[3][0]=2
    maze[3][1]=0
    maze[3][2]=2
    maze[3][3]=2
    maze[3][4]=2
    
    maze[4][0]=2
    maze[4][1]=0
    maze[4][2]=0
    maze[4][3]=0
    maze[4][4]=0
    
    i=0
    j=0
    
    while (i < size):
        j=0        
        while (j < size):     
            print(maze[i][j]),
            j=j+1
        i=i+1
        print(" ")




    # Maze Solver Function
    # k-> direction up, right, down, left
    # i,j -> position
    # count -> iteration
    def move(k,i,j,count):         
        
                
        while (count < 6):        
            if (count == 5):
                break
    
            # print current path
            l=0
            p=0
            while (l < size):
                p=0 
                while (p < size):     
                    if (l == i) and (p == j): 
                        print("#"),
                    else:
                        print(maze[l][p]),                
                    p=p+1
                l=l+1      
                print(" ")
                
            #print "k= ",k
            
            if (k == 5): k = 1
            
            if (k == 1):            
                m = i - 1
                n = j
                print("try to go up")
                
            if (k == 2):            
                m = i
                n = j + 1
                print("try to go right")
                
            if (k == 3):            
                m = i + 1
                n = j
                print("try to go down")
                
            if (k == 4):            
                m = i
                n = j - 1
                print("try to go left")
                
            print(" ")
            input("#################### Press Enter to continue...")
            print(" ")
            
            print("k ,","i ,","j ,","m ,","n ,","count ")
            print(k,",",i,",",j,",",m,",",n,",",count)
            print(" ")
            
            # print current path
    #        l=0
    #        p=0
    #        while (l < size):
    #            p=0        
    #            while (p < size):     
    #                if (l == i) and (p == j): 
    #                    print "#",
    #                else:
    #                    print maze[l][p],                
    #                p=p+1
    #            l=l+1      
    #            print " "
            
            
            if (n == size):
                print("SOLVED!")
                break
            
            if (maze[m][n] == 0) and (m != -1) and (n != -1) and (m != size):            
                print("success!")
                print(" ")
                maze[m][n] = 1
                move(1,m,n,1)            
            else:
                count = count + 1 
                print("fail") 
                print(" ")
                move(k+1,i,j,count)            
            k = k + 1
            
    # Solve Maze
    ##############
    
    # mark start point (as 1)
    maze[2][0] = 1
        
    # start solving
    move(1,2,0,1)
     
    # Print Maze after solve
    i=0
    j=0
    
    while (i < size):
        j=0        
        while (j < size):     
            print(maze[i][j]),
            j=j+1
        i=i+1
        print(" ")
    

else:
    import maze
    rawMaze = maze.createMaze(size, '2', '0')
    #pathMarker = ":grinning_face:" # :alien_monster: 
    pathMarker = ":zombie:"
    curMarker = ":alien_monster:" #":motorcycle:"#":zombie:" #":grinning_face:"
    maze = []
    showAdvance = True
    for i in range(size):
        maze.append(rawMaze[i*size+i:i*size+size+i]) ## '+i' -> skip the '\n'
        
        
        
    def markStep(maze, i,j): # marks step on a row i in position j
        tmp = list(maze[i])
        tmp[j] = emoji.emojize("%s"%pathMarker) #":alien_monster:")
        #tmp[j] = '~'
        maze[i] = "".join(tmp)

        
    # Maze Solver Function
    # k-> direction up, right, down, left
    # i,j -> position
    # count -> iteration
    def move(k,i,j,count):
        while (count < 6):        
            if (count == 5):
                break
                return False
    
            # print current path
            l=0
            p=0
            if showAdvance:
                while (l < size):
                    p=0
                    while (p < size):     
                        if (l == i) and (p == j): 
                            #print("# ", end=""),
                            #import emoji
                            print(emoji.emojize("%s"%curMarker), end=""),
                        else:
                            if maze[l][p] == emoji.emojize("%s"%pathMarker):
                                print("%s"%maze[l][p], end=""),
                            else:
                                print("%s "%maze[l][p], end=""),
                        p=p+1
                    l=l+1      
                    print(" ")
            
            #print "k= ",k
            
            if (k == 5): k = 1
            
            if (k == 1):            
                m = i - 1
                n = j
                print("try to go up")
                
            if (k == 2):            
                m = i
                n = j + 1
                print("try to go right")
                
            if (k == 3):            
                m = i + 1
                n = j
                print("try to go down")
                
            if (k == 4):            
                m = i
                n = j - 1
                print("try to go left")
                
            print(" ")
            time.sleep(0.001) #input("#################### Press Enter to continue...")
            print(" ")
            
            print("k ,","i ,","j ,","m ,","n ,","count ")
            print(k,",",i,",",j,",",m,",",n,",",count)
            print(" ")
            
            # print current path
            # l=0
            # p=0
            # while (l < size):
            #     p=0        
            #     while (p < size):     
            #        if (l == i) and (p == j): 
            #            print "#",
            #        else:
            #            print maze[l][p],                
            #        p=p+1
            #     l=l+1      
            #     print " "
            
            
            if (n == size):
                print("SOLVED!")
                return True
                break
            #import ipdb; ipdb.set_trace() 
            elif (maze[m][n] == '0') and (m != -1) and (n != -1) and (m != size):            
                print("success!")
                print(" ")
                #maze[m][n] = 1
                markStep(maze,m,n)
                ret = move(1,m,n,1)
            else:
                count = count + 1 
                print("fail")
                print(" ")
                ret = move(k+1,i,j,count)            
            if ret:
                return True
            k = k + 1
            
    # Solve Maze
    ##############
    
    # mark start point (as 1)
    print(rawMaze)
    #import ipdb; ipdb.set_trace()
    for i,L in enumerate(maze):
        if L[0] == "0":
            print("entrance row:%d"%i)
            row = i
            break


    #row = input("entarnce row: ")
    markStep(maze, int(row),0)
        
    #import ipdb; ipdb.set_trace()
    # start solving
    move(1,int(row),0,1)
    
    # Print Maze after solve
    i=0
    j=0
    
    while (i < size):
        j=0        
        while (j < size):     
            if maze[i][j] == emoji.emojize("%s"%pathMarker):
                print("%s"%maze[i][j], end="")
            else:
                print("%s "%maze[i][j], end=""),
            #print(maze[i][j]+" ", end=""),
            j=j+1
        i=i+1
        print(" ")
        
