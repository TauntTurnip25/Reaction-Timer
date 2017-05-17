from subprocess import call
import time
import os
from random import randint
def timer(time):
    print "press the 'enter key' when the message pops up."
    wait = randint(2, 5)
    time.sleep(wait)
    start = time.clock()
    a = raw_input("GO!!!!")
    finish = time.clock()
    time1 = finish - start
    time1 = round(time1, 3)
    time1 = time1 * 1000
    return time1

def table(times):
    print " Try | Time in milliseconds "
    print "----------------------------"
    for i in range(5):
        print "  " + str(i + 1) + "  |        " + str(times[i])
    print "  " + "Av." + "|        " + str(times[5])

times = []
for i in range(5):
    print "Try: " + str(i+1)
    time_in_milsec = timer(time)
    times.append(time_in_milsec)
    print "You scored " + str(time_in_milsec) + " milliseconds"
    time.sleep(2.5)
    os.system('cls')
x = 0
for j in times:
    x = x + j
x = x / 5
times.append(x)
table(times)
time.sleep(3.5)

