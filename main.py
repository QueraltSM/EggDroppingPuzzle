from time import time
import os
import sys
import memoization
import tabulation

show_time = False

def get_eggs_floors(path):
    file = open(path, 'r').read().split(",") # Saving data split
    eggs_floors = []
    for numbers in file:
        eggs_floors.append(int(numbers))
    return eggs_floors

def printTime(start):
    if show_time:
        print "Excecution time: ", (time() - start) * 1000, "milliseconds\n"

if os.path.isfile(sys.argv[1]):
    if len(sys.argv) == 3 and sys.argv[2] == "-t":
        show_time = True

    eggs_floors = get_eggs_floors(sys.argv[1])
    print "Minimum number of trials in worst case with",eggs_floors[0],"eggs and",eggs_floors[1],"floors is:"
    start = time()
    tabulation.init(eggs_floors[0], eggs_floors[1])
    printTime(start)
    start = time()
    memoization.init(eggs_floors[0], eggs_floors[1])
    printTime(start)

else:
    print "Error. Argument '",sys.argv[1],"' is not a file or it is not exists in the system"
