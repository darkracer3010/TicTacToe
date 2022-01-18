import time
import numpy as np
import sys
import colorama
from colorama import Fore
from simple_colors import *
def checkrow(mat,size):
    nump=np.array(mat)
    for i in range(size):
        if(np.all(nump[i]==nump[i][0])):
            return(nump[i][0])
        else:
            pass
def checkcol(mat,size):
    nump=np.array(mat)
    trans_nump=nump.T
    for i in range(size):
        if(np.all(trans_nump[i] == trans_nump[i][0])):
            return(trans_nump[i][0])
        else:
            pass
def checkdiag1(mat, size):
    s=""
    for i in range(size):
        s+=mat[i][i]
    if(s.count('X')==size or s.count('O')==size):
        return(s[0])
def checkdiag2(mat,size):
    io=""
    k=size-1
    for i in range(size):
        io+=mat[i][k]
        k-= 1
    if(io.count('X')==size or io.count('O')==size):
        return(io[0])
print("Hello players I hope You are ready for the game")
size=int(input("enter the size of the matrix:"))
print("Player-1 character selection")
player_1=input("Enter the character which you want to use within X and O:")
print("Player-2 character selection")
player_2=input("Enter the character which is not chosen by the Player-1:")
rows, cols = (size, size)
mat = [['_' for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        print(mat[i][j],end=" ")
    print()
print("The Game starts now:\n")
k=0
_pok_=0
_sok_=0
while(k<=size*size):
    print("A\'s turn, pick your spot:")
    po=time.time()
    q1=[i for i in input("Enter row,column:").split()]
    r=int(q1[0])-1
    c=int(q1[1])-1
    if(mat[r][c]=='_'):
        mat[r][c]=player_1
        _pok_=1
    else:
        iq=0
        while(_pok_!=1):
                print("This spot is taken already, pick an other spot")
                q1=[i for i in input("Enter row,column:").split()]
                r=int(q1[0])-1
                c=int(q1[1])-1
                if(mat[r][c]=='_'):
                    mat[r][c]=player_1
                    _pok_=1
                iq+=1
                if(iq==1):
                    print("\nFinal Warning:Dont Repeat it again\n")
                if(iq==2):
                    print("Your Fault player-2 is the winner")
                    sys.exit()
    t=time.time()
    _pok_=0
    z=checkrow(mat,size)
    x=checkcol(mat,size)
    fk=checkdiag1(mat,size)
    lk=checkdiag2(mat,size)
    if(t-po<15):
        if(z!=None):
            if(z==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(z==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(x!=None):
            if(x==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(x==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(fk!=None):
            if(fk==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(fk==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(lk!=None):
            if(lk==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(lk==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(k==size+1 and (lk==None and fk==None and x==None and z==None)):
            print("It is a tie , gg")
            sys.exit()
        print("The matrix is:\n")
        for i in range(rows):
            for j in range(cols):
                print(mat[i][j],end=" ")
            print()
    else:
        print("time-up player-2 is the winner, player-1 has some better things to do")
        sys.exit()
    time.sleep(5)
    print("B\'s turn, pick your spot:")
    oy=time.time()
    q2=[i for i in input("Enter row,column:").split()]
    ro=int(q2[0])-1
    co=int(q2[1])-1
    if(mat[ro][co]=='_'):
        mat[ro][co]=player_2
    else:
        iq=0
        while(_sok_!=1):
                print("This spot is taken already, pick an other spot")
                q2=[i for i in input("Enter row,column:").split()]
                ro=int(q2[0])-1
                co=int(q2[1])-1
                if(mat[ro][co]=='_'):
                    mat[ro][co]=player_2
                    _sok_=1
                iq+=1
                if(iq==1):
                    print('\033[1m'+"Dont Repeat it again"+'\033[1m')
                if(iq==2):
                    print("Your Fault player-1 is the winner")
                    sys.exit()
    _sok_=0
    yo=time.time()
    zk=checkrow(mat,size)
    xk=checkcol(mat,size)
    ik=checkdiag1(mat,size)
    sk=checkdiag2(mat,size)
    if(yo-oy<15):
        if(zk!=None):
            if(zk==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(zk==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(xk!=None):
            if(xk==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(xk==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(ik!=None):
            if(ik==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(ik==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(sk!=None):
            if(sk==player_1):
                print("Player-1 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            elif(sk==player_2):
                print("Player-2 is the winner")
                print("The final matrix is:\n")
                for i in range(rows):
                    for j in range(cols):
                        print(mat[i][j],end=" ")
                    print()
                sys.exit()
            else:
                pass
        elif(k==size+1 and(zk==None and xk==None and ik==None and sk==None)):
            print("It is a tie, gg")
        print("The matrix is:\n")
        for i in range(rows):
            for j in range(cols):
                print(mat[i][j],end=" ")
            print()
    else:
        print("time-up player-1 is the winner, player-2 considers this match as pointless")
        sys.exit()
    time.sleep(5)
    k+=1
