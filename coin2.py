import sys
import random

def flip(p):
    #  p will change between .5 and .75 depending on fair or biased coin
    #  but any probability value will work
    return 'H' if random.random() < p else 'T'

def transition(state):
    #  p will change between .5 and .75 depending on fair or biased coin
    #  but any probability value will work
    change=random.random()
    if change <= 0.10:
        if state == 'F':
           print("Changing from ",state," to B")
           return 'B' 
        else: 
           print("Changing from ",state," to F")
           return 'F' 
    return state

def main():
    print("Hidden markov models")
    print("Fair or bias coin? sequence")

    transitionDict={('F','F'):0.9,('F','B'):0.10,('B','F'):0.10,('B','B'):0.9}
    emissionDict={('F','H'):0.5,('F','T'):0.50,('B','H'):0.75,('B','T'):0.25}

    print("--------------------")
    print("Start flip sims: Fair")
    Hcount=0
    Tcount=0
    p=0.75
    p=0.5
    state='F'
    for y in range(100):
        # simulate a coin change window of set flip number of 100
        state=transition(state)
        if state=='F':
            p=0.5
        else :
            p=0.75 
        for x in range(100):
           result=flip(p)
           if result=='H':
              Hcount+=1
           else: 
              Tcount+=1

        print(Hcount," heads and ",Tcount," tails")
        Hcount=0
        Tcount=0


    print("bye ")

if __name__ == "__main__":
    main()
