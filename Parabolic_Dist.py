#! /usr/bin/env python
from Random import Random
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    i =0
    random = Random(66666)
    valuelist = []
    while i<1000:

        #print (random.Exponential(i),"exponential")
        #print (random.Color_Baloon(),"my color")
        #color = random.Color_Baloon()
        x = random.parabolic_dist(10.)
        #x = random.Exponential(10.)
        #print (x)
        #color =random.Bernoulli(0.5)
        valuelist.append(x)
        #print (color)
        i=i+1

    n, bins, patches = plt.hist(valuelist, 20, density=True, facecolor='r', alpha=0.75)
    #print (n)
    plt.xlabel('x')
    plt.ylabel('Probability/20 bin')
    plt.title('Generated Random Numbers with parabolic distribution ')
    plt.grid(True)
    print("saving histograms to file parabola.png")
    plt.savefig("parabola.png")
    plt.show()
