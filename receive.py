#Based on the code from: http://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/?ALLSTEPS
from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
import pickle

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 7
RECEIVE_PIN = 27

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print '**Started recording**'
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.seconds
    print '**Ended recording**'
    print len(RECEIVED_SIGNAL[0]), 'samples recorded'
    GPIO.cleanup()

    print '**Processing results**'
    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds/1000000.0

    print '**Plotting results**'
    #If you don't have X copy the pickle to a machine that does and use the load.py script to visulize the data
    pickle.dump(RECEIVED_SIGNAL,open( "save.p", "wb" ))
    #Uncomment this if you run this script in an X capable machine
    #pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
    #pyplot.axis([0, MAX_DURATION, -1, 2])
    #pyplot.show()
