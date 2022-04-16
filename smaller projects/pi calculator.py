from random import randint
from math import floor
from time import time

def monteCarlo():
    Pout=0
    tests=int(input("Number of tests: "))
    #currently runs at ~280,000 numbers/second
    print("estimated run time at "+str(floor(tests/280000))+" seconds")
    startTime = time()

    for i in range(0,tests):
        x=randint(1,10000000000000)
        x=x/10000000000000
        y=randint(1,10000000000000)
        y=y/10000000000000
        if x**2 + y**2 > 1:
            Pout += 1

    Pin = tests-Pout
    print (floor(time() - startTime), "seconds to run")
    #print ("Number of points in ("+str(Pin)+") and number out ("+str(Pout)+")")
    print("Pi approximation = "+str((4*Pin)/tests))

monteCarlo()
