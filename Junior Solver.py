# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:11:28 2017

@author: Paul
"""
#Solveur de Pocket Cube

print("""
                           ____  ___   __________  ____     _    __   ___        ____
                          / / / / / | / /  _/ __ \/ __ \   | |  / /  <  /       / __ \
                     __  / / / / /  |/ // // / / / /_/ /   | | / /   / /       / / / /
                    / /_/ / /_/ / /|  // // /_/ / _, _/    | |/ /   / /  _    / /_/ /
                    \____/\____/_/ |_/___/\____/_/ |_|     |___/   /_/  (_)   \____/




                     2
                     ^
                     I   -3
                     I  /
                     I /
                     I/
      -1 <-----------------------> 1
                    /I
                   / I
                  /  I
                 3   I
                     v
                    -2


NASSIM FOUADH - PAUL SKAF - ANTOINE LE GOHALEN - FABIEN VERDIER


""")
print( 'On lit le cube en partant du coin haut gauche, sens inverse des aiguilles d une montre')
print ('puis coin bas droit pour finir les 4 pieces restantes')

dicooriens={1:2,2:2,3:2,4:2,5:-2,6:-2,7:-2,8:-2} #orientation du cube resolu
cuberes=[1,2,3,4,5,6,7,8] #position du cube resolu
move=[]

def U(liste,dico) : #mouvement U
    ndico={}
    ncube=[]
    ncube.append(liste[1])
    ncube.append(liste[2])
    ncube.append(liste[3])
    ncube.append(liste[0])
    ncube.append(liste[4])
    ncube.append(liste[5])
    ncube.append(liste[6])
    ncube.append(liste[7])
    for i in range(4,8):
        ndico[liste[i]]=dico[liste[i]]
        del dico[liste[i]]
    for i in dico :
        if dico[i]==-3:
            ndico[i]=1
        if dico[i]==1:
            ndico[i]=3
        if dico[i]==3:
            ndico[i]=-1
        if dico[i]==-1:
            ndico[i]=-3
        if dico[i]==2:
            ndico[i]=2
        if dico[i]==-2:
            ndico[i]=-2
    move.append("U")
    return ncube,ndico

def Up(liste,dico): #mouvement U prime
    for i in range(0,3):
        liste,dico=U(liste,dico)
    move.append("U'")
    return liste,dico

def D(liste,dico): #mouvement D
    ncube=[]
    ndico={}
    ncube.append(liste[0])
    ncube.append(liste[1])
    ncube.append(liste[2])
    ncube.append(liste[3])
    ncube.append(liste[7])
    ncube.append(liste[4])
    ncube.append(liste[5])
    ncube.append(liste[6])
    for i in range(0,4):
        ndico[liste[i]]=dico[liste[i]]
        del dico[liste[i]]
    for i in dico :
        if dico[i]==1:
            ndico[i]=-3
        if dico[i]==-3:
            ndico[i]=-1
        if dico[i]==-1:
            ndico[i]=3
        if dico[i]==3:
            ndico[i]=1
        if dico[i]==-2:
            ndico[i]=-2
        if dico[i]==2:
            ndico[i]=2
    move.append("D")
    return ncube,ndico

def Dp(liste,dico): #mouvement D prime
    for i in range(0,3):
        liste,dico=D(liste,dico)
    move.append("D'")
    return liste,dico

def F(liste,dico): #mouvement F
    ncube=[]
    ndico={}
    ncube.append(liste[4])
    ncube.append(liste[0])
    ncube.append(liste[2])
    ncube.append(liste[3])
    ncube.append(liste[5])
    ncube.append(liste[1])
    ncube.append(liste[6])
    ncube.append(liste[7])
    for i in [2,3,6,7] :
        ndico[liste[i]]=dico[liste[i]]
        del dico[liste[i]]
    for i in dico :
        if dico[i]==2:
            ndico[i]=1
        if dico[i]==1:
            ndico[i]=-2
        if dico[i]==-2:
            ndico[i]=-1
        if dico[i]==-1:
            ndico[i]=2
        if dico[i]==3:
            ndico[i]=3
        if dico[i]==-3:
            ndico[i]=-3
    move.append("F")
    return ncube,ndico

def Fp(liste,dico): #mouvement F prime
    for i in range(0,3):
        liste,dico=F(liste,dico)
    move.append("F'")
    return liste,dico

def B(liste,dico):
    ncube=[]
    ndico={}
    ncube.append(liste[0])
    ncube.append(liste[1])
    ncube.append(liste[6])
    ncube.append(liste[2])
    ncube.append(liste[4])
    ncube.append(liste[5])
    ncube.append(liste[7])
    ncube.append(liste[3])
    for i in [0,1,4,5] :
        ndico[liste[i]]=dico[liste[i]]
        del dico[liste[i]]
    for i in dico :
        if dico[i]==2:
            ndico[i]=-1
        if dico[i]==-1:
            ndico[i]=-2
        if dico[i]==-2:
            ndico[i]=1
        if dico[i]==1:
            ndico[i]=2
        if dico[i]==3:
            ndico[i]=3
        if dico[i]==-3:
            ndico[i]=-3
    move.append("B")
    return ncube,ndico

def Bp(liste,dico): #mouvement B prime
    for i in range(0,3):
        liste,dico=B(liste,dico)
    move.append("B'")
    return liste,dico

def R(liste,dico): #mouvement R prime
    ncube=[]
    ndico={}
    ncube.append(liste[0])
    ncube.append(liste[5])
    ncube.append(liste[1])
    ncube.append(liste[3])
    ncube.append(liste[4])
    ncube.append(liste[6])
    ncube.append(liste[2])
    ncube.append(liste[7])
    for i in [0,3,7,4] :
        ndico[liste[i]]=dico[liste[i]]
        del dico[liste[i]]
    for i in dico :
        if dico[i]==2:
            ndico[i]=-3
        if dico[i]==-3:
            ndico[i]=-2
        if dico[i]==-2:
            ndico[i]=3
        if dico[i]==3:
            ndico[i]=2
        if  dico[i]==-1:
            ndico[i]=-1
        if dico[i]==1:
            ndico[i]=1
    move.append("R")
    return ncube,ndico

def Rp(liste,dico): #mouvement R prime
    for i in range(0,3):
        liste,dico=R(liste,dico)
    move.append("R'")
    return liste,dico


def L(liste,dico): #mouvement L
    ncube=[]
    ndico={}
    ncube.append(liste[3])
    ncube.append(liste[1])
    ncube.append(liste[2])
    ncube.append(liste[7])
    ncube.append(liste[0])
    ncube.append(liste[5])
    ncube.append(liste[6])
    ncube.append(liste[4])
    for i in [1,2,5,6]:
        ndico[liste[i]]=dico[liste[i]]
        del dico[liste[i]]
    for i in dico :
        if dico[i]==2:
            ndico[i]=3
        if dico[i]==3:
            ndico[i]=-2
        if dico[i]==-2:
            ndico[i]=-3
        if dico[i]==-3:
            ndico[i]=2
        if dico[i]==1:
            ndico[i]=1
        if dico[i]==-1:
            ndico[i]=-1
    move.append("L")
    return ncube,ndico

def Lp(liste,dico): #mouvement L prime
    for i in range(0,3) :
        liste,dico=L(liste,dico)
    move.append("L'")
    return liste,dico

'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
def cube2(liste,dico):
    if liste[3]==cuberes[1] :
        (liste,dico)=B(liste,dico)
        (liste,dico)=B(liste,dico)
        (liste,dico)=R(liste,dico)
        (liste,dico)=R(liste,dico)
        return liste,dico
    i=0
    while i<=3 and liste[1]!=cuberes[1] :
        liste,dico=R(liste,dico)
        i+=1
    if liste[1]==cuberes[1] :
        if dico[liste[1]]==2  :
            return liste,dico
        elif dico[liste[1]]==1 :
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            liste,dico=D(liste,dico)
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            return liste,dico
        elif dico[liste[1]]==3:
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            liste,dico=D(liste,dico)
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            liste,dico=D(liste,dico)
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            return liste,dico
    i=0
    move.remove("R")
    move.remove("R")
    move.remove("R")
    move.remove("R")
    while i<=3 and liste[1]!=cuberes[1] :
        liste,dico=D(liste,dico)
        liste,dico=R(liste,dico)
        i+=1
    if liste[1]==cuberes[1] :
        if dico[liste[1]]==2  :
            return liste,dico
        elif dico[liste[1]]==1 :
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            liste,dico=D(liste,dico)
            liste,dico=Rp(liste,dico)
            liste,dico=Dp(liste,dico)
            liste,dico=R(liste,dico)
            return liste,dico
        elif dico[liste[1]]==3 :
            (liste,dico)=Rp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=R(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Rp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=R(liste,dico)
            return liste,dico

def cube3(liste,dico) :
    if liste[2]==cuberes[2] :
        if dico[liste[2]]==2 :
            return liste,dico
        if dico[liste[2]]==1 :
            (liste,dico)=B(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=B(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Bp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=B(liste,dico)
            return liste,dico
        if dico[liste[2]]==-3 :
            (liste,dico)=R(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Rp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=R(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Rp(liste,dico)
            return liste,dico
    elif liste[2]!=cuberes[2]:
        i=0
        while liste[6]!=cuberes[2] and i <=3 :
            (liste,dico)=D(liste,dico)
            i+=1
        if liste[6]==cuberes[2] :
            if dico[liste[6]]==1 :
                (liste,dico)=R(liste,dico)
                (liste,dico)=D(liste,dico)
                (liste,dico)=Rp(liste,dico)
                return liste,dico
            elif dico[liste[6]]==-3 :
                (liste,dico)=Bp(liste,dico)
                (liste,dico)=Dp(liste,dico)
                (liste,dico)=B(liste,dico)
                return liste,dico
            elif dico[liste[6]]==-2 :
                (liste,dico)=R(liste,dico)
                (liste,dico)=D(liste,dico)
                (liste,dico)=D(liste,dico)
                (liste,dico)=Rp(liste,dico)
                (liste,dico)=Dp(liste,dico)
                (liste,dico)=R(liste,dico)
                (liste,dico)=D(liste,dico)
                (liste,dico)=Rp(liste,dico)
                return liste,dico

        elif liste[3]==cuberes[2] :
            if dico[liste[3]]==-1 :
                (liste,dico)=Bp(liste,dico)
                return liste,dico
            elif dico[liste[3]]==2 :
                (liste,dico)=B(liste,dico)
                (liste,dico)=R(liste,dico)
                (liste,dico)=Dp(liste,dico)
                (liste,dico)=Rp(liste,dico)
                return liste,dico
            elif dico[liste[3]]==-3 :
                (liste,dico)=B(liste,dico)
                (liste,dico)=Dp(liste,dico)
                (liste,dico)=B(liste,dico)
                return liste,dico

def cube4(liste,dico):
    if liste[3]==cuberes[3] :
        if dico[liste[3]]==2  :
            return liste,dico
        if dico[liste[3]]==-1 :
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=L(liste,dico)
            return liste,dico
        if dico[liste[3]]==-3 :
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=L(liste,dico)
            return liste,dico

    elif liste[3]!=cuberes[3] :
        i=0
        while liste[7]!=cuberes[3] and i<=3:
            (liste,dico)=D(liste,dico)
            i+=1

        if dico[liste[7]]==-1 :
           (liste,dico)=Lp(liste,dico)
           (liste,dico)=Dp(liste,dico)
           (liste,dico)=L(liste,dico)
           return liste,dico
        elif dico[liste[7]]==-3:
            (liste,dico)=B(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=Bp(liste,dico)
            return liste,dico
        elif dico[liste[7]]==-2 :
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=L(liste,dico)
            return liste,dico
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'

#ORIENTATION DERNIERE FACE
dicoalgo={"sun":"L D L' D L D D L'","antisun":"L D D L' D' L D' L'","pi":"F L D L' D' L D L' D' F'","T":"F L D L' D' F'","Tp":"L D L' D' L' F L F'","fish":"F L' F' L D L D' L'","H":"R R D D R D D R R" }

def sun(liste,dico):
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    for i in range(0,14):
        del move[-1]
    return liste,dico

def antisun(liste,dico) :
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=Lp(liste,dico)
    for i in range(0,20):
        del move[-1]
    return liste,dico

def pi(liste,dico) :
    (liste,dico)=F(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=Fp(liste,dico)
    for i in range(0,25):
        del move[-1]
    return liste,dico

def T(liste,dico):
    (liste,dico)=F(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=Fp(liste,dico)
    for i in range(0,15):
        del move[-1]
    return liste,dico

def Tp(liste,dico) :
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=F(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=Fp(liste,dico)
    for i in range(0,20):
        del move[-1]
    return liste,dico

def fish(liste,dico):
    (liste,dico)=F(liste,dico)
    (liste,dico)=Lp(liste,dico)
    (liste,dico)=Fp(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=L(liste,dico)
    (liste,dico)=Dp(liste,dico)
    (liste,dico)=Lp(liste,dico)
    for i in range(0,20):
        del move[-1]
    return liste,dico

def H(liste,dico):
    (liste,dico)=R(liste,dico)
    (liste,dico)=R(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=R(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=D(liste,dico)
    (liste,dico)=R(liste,dico)
    (liste,dico)=R(liste,dico)
    for i in range(0,9):
        del move[-1]
    return liste,dico

'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'

def orientation(liste,dico) :
    r=0
    while r!=1:
        if dico[liste[4]]==dico[liste[5]]==dico[liste[6]]==dico[liste[7]]==-2 :
            r=1
            return liste,dico

        elif dico[liste[4]]==dico[liste[5]]==3 and dico[liste[6]]==dico[liste[7]]==-3 :
            (liste,dico)=H(liste,dico)
            r=1
            move.append(dicoalgo["H"])
            return liste,dico
        elif dico[liste[4]]==3 and dico[liste[5]]==-2 and dico[liste[6]]==-3 and dico[liste[7]]==-1 :
            (liste,dico)=sun(liste,dico)
            r=1
            move.append(dicoalgo["sun"])
            return liste,dico
        elif dico[liste[4]]==-1 and dico[liste[5]]==3 and dico[liste[6]]==1 and dico[liste[7]]==-2 :
            (liste,dico)=antisun(liste,dico)
            r=1
            move.append(dicoalgo["antisun"])
            return liste,dico
        elif dico[liste[4]]==3 and dico[liste[5]]==dico[liste[6]]==1 and dico[liste[7]]==-3 :
            (liste,dico)=pi(liste,dico)
            r=1
            move.append(dicoalgo["pi"])
            return liste,dico
        elif dico[liste[4]]==-2 and dico[liste[5]]==1==dico[liste[6]] and dico[liste[7]]==-2 :
            (liste,dico)=T(liste,dico)
            r=1
            move.append(dicoalgo["T"])
            return liste,dico
        elif dico[liste[4]]==-2 and dico[liste[5]]==3 and dico[liste[6]]==-2 and dico[liste[7]]==-1 :
            (liste,dico)=fish(liste,dico)
            r=1
            move.append(dicoalgo["fish"])
            return liste,dico
        elif dico[liste[4]]==-2 and dico[liste[5]]==3 and dico[liste[6]]==-3 and dico[liste[7]]==-2 :
            (liste,dico)=Tp(liste,dico)
            r=1
            move.append(dicoalgo["Tp"])
            return liste,dico
        if r!=1:
            (liste,dico)=D(liste,dico)

'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'

def position(liste,dico):
    z=0
    while z!=1:
        if (liste[4]==cuberes[4] and liste[6]==cuberes[6] and liste[5]==cuberes[5] and liste[7]==cuberes[7]) or (liste[4]==cuberes[5] and liste[5]==cuberes[6] and liste[6]==cuberes[7] and liste[7]==cuberes[4]) or (liste[4]==cuberes[6] and liste[5]==cuberes[7] and liste[6]==cuberes[4] and liste[7]==cuberes[5])or(liste[4]==cuberes[7] and liste[5]==cuberes[4] and liste[6]==cuberes[5] and liste[7]==cuberes[6]):
            z=1
            return liste,dico
        elif (liste[4]==cuberes[6] and liste[6]==cuberes[4] and liste[5]==cuberes[5] and liste[7]==cuberes[7])or(liste[4]==cuberes[7] and liste[5]==cuberes[6] and liste[6]==cuberes[5] and liste[7]==cuberes[4])or(liste[4]==cuberes[4] and liste[5]==cuberes[7] and liste[6]==cuberes[6] and liste[7]==cuberes[5])or(liste[4]==cuberes[5] and liste[5]==cuberes[4] and liste[6]==cuberes[7] and liste[7]==cuberes[6]) :
            (liste,dico)=F(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Fp(liste,dico)
            (liste,dico)=Tp(liste,dico)
            z=1
            move.append(dicoalgo["Tp"])
            return liste,dico
        elif (liste[4]==cuberes[7] and liste[5]==cuberes[5] and liste[6]==cuberes[6] and liste[7]==cuberes[4])or(liste[4]==cuberes[4] and liste[5]==cuberes[6] and liste[6]==cuberes[7] and liste[7]==cuberes[5]) or (liste[4]==cuberes[5] and liste[5]==cuberes[7] and liste[6]==cuberes[4] and liste[7]==cuberes[6]) or (liste[4]==cuberes[6] and liste[5]==cuberes[4] and liste[6]==cuberes[5] and liste[7]==cuberes[7]):
            (liste,dico)=L(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=F(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Dp(liste,dico)
            (liste,dico)=L(liste,dico)
            (liste,dico)=D(liste,dico)
            (liste,dico)=Lp(liste,dico)
            (liste,dico)=Fp(liste,dico)
            z=1
            return liste,dico

        elif z!=1:
            (liste,dico)=D(liste,dico)

'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
def propre(move):
    l=0
    count=0
    a,b,c,d,e,f="D","U","F","L","R","B"
    for i in move:
        if i=="D" and a=="D":
            count=count+1
            a=i
        elif count>=3 and i=="D'":
            del move[l-1]
            del move[l-2]
            del move[l-3]
        elif i=="R" and e=="R":
            count=count+1
            e=i
        elif count>=3 and i=="R'":
            del move[l-1]
            del move[l-2]
            del move[l-3]
        elif i=="U" and b=="U":
            count=count+1
            b=i
        elif count>=3 and i=="U'":
            del move[l-1]
            del move[l-2]
            del move[l-3]
        elif i=="F" and c=="F":
            count=count+1
            c=i
        elif count>=3 and i=="F'":
            del move[l-1]
            del move[l-2]
            del move[l-3]
        elif i=="L" and d=="L":
            count=count+1
            d=i
        elif count>=3 and i=="L'":
            del move[l-1]
            del move[l-2]
            del move[l-3]
        elif i=="B" and f=="B":
            count=count+1
            f=i
        elif count>=3 and i=="B'":
            del move[l-1]
            del move[l-2]
            del move[l-3]
        else:
            count=0
        l=l+1
    return move
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
'----------------------------------------------------------------------'
cubenrestuple=input("Entrez les 8 postions du cube dans l'ordre, chaque chiffre separe par une virgule :")
oriencubenrestuple=input("Entrez les 8 orientations separe d'une virgule :")
cubenres,oriennres=list(cubenrestuple),list(oriencubenrestuple)#transformation des tuples  en liste
cubenrestuple,oriencubenrestuple=None,None #suppresion des 2 tuples
diconorien={}
for i in enumerate(cubenres) :
    diconorien[i[1]]=oriennres[i[0]]
i,oriennres=None,None

(cubenres,diconorien)=cube2(cubenres,diconorien)
(cubenres,diconorien)=cube3(cubenres,diconorien)
(cubenres,diconorien)=cube4(cubenres,diconorien)
(cubenres,diconorien)=orientation(cubenres,diconorien)
(cubenres,diconorien)=position(cubenres,diconorien)

while cuberes!=cubenres :
    (cubenres,diconorien)=D(cubenres,diconorien)

move=propre(move)
for p in move :
    print (p)
print ("Nombre de mouvements : ", len(move))
print ("Cube Resolu")
print (cubenres,diconorien)


