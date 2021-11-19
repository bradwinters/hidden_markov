import sys
import random

def flipB():
    random_number = random.randint(1,4)
    if random_number > 1:
       return 'H'
    return 'T'

def flipF():
    random_number = random.randint(1,2)
    if random_number > 1:
       return 'T'
    return 'H'

def main():
    print("Hidden markov models")
    print("Fair or bias coin sequence")

    fair_coin=False

    transitionDict={('F','F'):0.9,('F','B'):0.10,('B','F'):0.10,('B','B'):0.9}
    emissionDict={('F','H'):0.5,('F','T'):0.50,('B','H'):0.75,('B','T'):0.25}

    prob =transitionDict[('F','F')]
    print(prob)

    prob =emissionDict[('B','T')]
    print(prob)
    print("--------------------")
    print("Start flip sims: Fair")
    Hcount=0
    Tcount=0
    for y in range(100):
        for x in range(100):
           if fair_coin==True:
               result=flipF()
           else:
               result=flipB()
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
