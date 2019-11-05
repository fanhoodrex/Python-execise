import random

def printintro():
    print('this program simulate 2 player in particular game')
    print('program should take the value of A and B (0-1 )')
    
def getinput():
    a = eval (input('enter the value of PlayerA(0-1):'))
    b = eval (input('enter the value of PlayerB(0-1):'))
    c = eval (input('total times of simulation:'))
    return a,b,n



def printSummary(winsA,winsB):
    n = winsA+winsB
    print('Analysis for competition start,totally simulate{}',format(n))
    print('playerA win {} times in game, taking up {:0.1%}'.format(winsA,winsA/n))
    print('playerB win {} times in game, taking up {:0.1%}'.format(winB,winB/n))

def gameover(a,b):
    return a==15 or b ==15




def simOneGame(proA,proB):
    scoreA,scoreB = 0 , 0
    serving ='A'
    while not gameover(scoreA,scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving ='B'
        else:
            if random() <proB:
                scoreB+=1
            else:
                serving = 'A'
                
    return scoreA,scoreB

def simNGames(n,proA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(proA,proB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def main():
    printintro()
    proA,proB,n=getinput=()
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)

main()
