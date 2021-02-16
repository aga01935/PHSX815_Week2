#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":

    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True

    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)

    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True

    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue

            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)




    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    #calculating the quantiles
    median = np.median(times_avg)
    onesigmaplus =median + np.std(times_avg)
    onesigmaminus = median - np.std(times_avg)

    twosigmaplus =median + 2*np.std(times_avg)
    twosigmaminus = median - 2*np.std(times_avg)

    threesigmaplus = median + 3*np.std(times_avg)
    threesigmaminus = median - 3*np.std(times_avg)
    #print(median)


    plt.figure()
    #n, bins, patches =
    plt.hist(times, 100, density=True, facecolor='r', alpha=0.75)
    #print (n)
    plt.xlabel('Time between the dissappearence of the cookies(Days)')
    plt.ylabel('Probability')
    plt.title(' ')
    plt.grid(True)
    print("saving histograms to file")
    plt.savefig("Time.png")
    #plt.show()

    plt.figure()
    plt.hist(times_avg, 100, range= (0,2.5),density=True, facecolor='g', alpha=0.75)
    #print (n)
    plt.xlabel('Time Average')
    plt.ylabel('Probability')
    plt.title('Generated Random Numbers with parabolic distribution ')
    plt.grid(True)
    min_ylim, max_ylim = plt.ylim()
    plt.axvline(median, color='r', linestyle='dashed', linewidth=1)
    plt.text(median*1.01, max_ylim*0.7, 'Median: {:.2f}'.format(median),rotation = 90)

    plt.axvline(onesigmaplus, color='b', linestyle='dashed', linewidth=1)
    plt.text(onesigmaplus*1.01, max_ylim*0.7, ' +1 $\sigma$= {:.2f}'.format(onesigmaplus),rotation = 90)

    plt.axvline(onesigmaminus, color='b', linestyle='dashed', linewidth=1)
    plt.text(onesigmaminus*1.01, max_ylim*0.7, '-1 $\sigma$= {:.2f}'.format(onesigmaminus),rotation = 90)

    plt.axvline(twosigmaplus, color='b', linestyle='dashed', linewidth=1)
    plt.text(twosigmaplus*1.01, max_ylim*0.7, ' +2 $\sigma$= {:.2f}'.format(twosigmaplus),rotation = 90)

    plt.axvline(twosigmaminus, color='b', linestyle='dashed', linewidth=1)
    plt.text(twosigmaminus*1.01, max_ylim*0.7, '-2 $\sigma$= {:.2f}'.format(twosigmaminus),rotation = 90)

    plt.axvline(threesigmaplus, color='b', linestyle='dashed', linewidth=1)
    plt.text(threesigmaplus*1.01, max_ylim*0.7, ' +3 $\sigma$= {:.2f}'.format(threesigmaplus),rotation = 90)

    plt.axvline(threesigmaminus, color='b', linestyle='dashed', linewidth=1)
    plt.text(threesigmaminus*1.01, max_ylim*0.7, '-3 $\sigma$= {:.2f}'.format(threesigmaminus),rotation = 90)

    plt.savefig("Time_Average.png")
    plt.show()
