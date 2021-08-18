import time
import numpy as np
import sys
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
    if(s.count('X')==3 or s.count('O')==3):
        return(s[0])
def checkdiag2(mat,size):
    io=""
    k=size-1
    for i in range(size):
        io+=mat[i][k]
        k-= 1
    if(io.count('X')==3 or io.count('O')==3):
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
#print(len(mat))
print("The Game starts now:\n")
k=0
_pok_=0
_sok_=0
while(k<=size*size):
    print("A\'s turn, pick your spot:")
    po=time.time()
    r,c=int(input()),int(input())
    if(mat[r][c]=='_'):
        mat[r][c]=player_1
        _pok_=1
    else:
        while(_pok_!=1):
            print("This spot is taken already, pick an other spot")
            r,c=int(input()),int(input())
            if(mat[r][c]=='_'):
                mat[r][c]=player_1
                _pok_=1
    _pok_=0
    print("The matrix is:\n")
    for i in range(rows):
        for j in range(cols):
            print(mat[i][j],end=" ")
        print()
    t=time.time()
    z=checkrow(mat,size)
    x=checkcol(mat,size)
    fk=checkdiag1(mat,size)
    lk=checkdiag2(mat,size)
    if(t-po<30):
        if(z!=None):
            if(z==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(z==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
        elif(x!=None):
            if(x==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(x==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
        elif(fk!=None):
            if(fk==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(fk==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
        elif(lk!=None):
            if(lk==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(lk==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
    else:
        print("time-up player-2 is the winner, player-1 has some better things to do")
        sys.exit()
    time.sleep(5)
    print("B\'s turn, pick your spot:")
    oy=time.time()
    ro,co=int(input()),int(input())
    if(mat[ro][co]=='_'):
        mat[ro][co]=player_2
    else:
        while(_sok_!=1):
            print("This spot is taken already, pick an other spot")
            ro,co=int(input()),int(input())
            if(mat[ro][co]=='_'):
                mat[ro][co]=player_2
                _sok_=1
    _sok_=0
    print("The matrix is:\n")
    for i in range(rows):
        for j in range(cols):
            print(mat[i][j],end=" ")
        print()
    yo=time.time()
    zk=checkrow(mat,size)
    xk=checkcol(mat,size)
    ik=checkdiag1(mat,size)
    sk=checkdiag2(mat,size)
    if(yo-oy<30):
        if(zk!=None):
            if(zk==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(zk==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
        elif(xk!=None):
            if(xk==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(xk==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
        elif(ik!=None):
            if(ik==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(ik==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
        elif(sk!=None):
            if(sk==player_1):
                print("Player-1 is the winner")
                sys.exit()
            elif(sk==player_2):
                print("Player-2 is the winner")
                sys.exit()
            else:
                pass
    else:
        print("time-up player-1 is the winner, player-2 considers this match as pointless")
        sys.exit()
    time.sleep(5)
    k+=1
