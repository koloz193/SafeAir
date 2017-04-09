from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_gas as upmGas

def main():
    front = upmGas.MQ5(1)
    right = upmGas.MQ3(2)
    left = upmGas.MQ3(0)

    threshContext = upmGas.thresholdContext()

    global current_level

    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit, including functions from myMQ5
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    while(1):
        left_reading = left.getSample()
        front_reading = front.getSample()
        right_reading = right.get_Sample()

        # add conditional for if 2 of 3 senors are equal
        if left_reading <= current_level and right_reading <= current_level and front_reading <= current_level:
            if current_level is None:

            else:

            return
        else if left_reading > right_reading and left_reading > front_reading:
            current_level = left_reading
            # move left
        else if right_reading > left_reading and right_reading > front_reading:
            current_level = right_reading
            # move right
        else if front_reading >= left_reading and front_reading >= right_reading:
            current_level = front_reading
            # move forward


if __name__ == '__main__':
    main()
