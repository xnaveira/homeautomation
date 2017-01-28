import pickle
import matplotlib.pyplot as pyplot 
import sys

MAX_DURATION = 5
RECEIVED_SIGNAL = pickle.load(open(sys.argv[1], "rb"))
pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
pyplot.axis([0, MAX_DURATION, -1, 2])
pyplot.show()
