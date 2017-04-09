from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_gas as upmGas
import sms_notify
import os

# Values are mean of 1000 readings
mq3_norm = 899.0575
mq5_norm = 531.52125

mq3_sensor = upmGas.MQ3(0) # left sensor
mq5_sensor = upmGas.MQ5(1)

def get_mq3_level():
    return mq3_sensor.getSample()

def get_mq5_level():
    return mq5_sensor.getSample()

def passive_scan():
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
    new_pid = os.fork()

    total = 0

    if new_pid == 0:
        level = get_mq3_level()
        while (level < (mq3_norm * 0.65)):
            level = get_mq3_level()
        sms_notify.send_gas_detected("MQ3 Alcohol, Ethanol, Smoke Sensor")
        return
    else:
        level = get_mq5_level()
        while (level < (mq5_norm * 0.65)):
            level = get_mq5_level()
        sms_notify.send_gas_detected("MQ5 Natural Gas and Liquefied Petroleum Gas (LPG) Sensor")
        return

if __name__ == '__main__':
    passive_scan()
