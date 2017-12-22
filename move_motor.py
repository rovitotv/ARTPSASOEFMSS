#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import argparse

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--direction', required=True, default=None, help=
        ('direction either forward or backward'))
    args = parser.parse_args()
    myMotor = mh.getMotor(1)
    myMotor.setSpeed(100)
    if args.direction == 'forward':
        myMotor.run(Adafruit_MotorHAT.FORWARD);    
    elif args.direction == 'backward':
        myMotor.run(Adafruit_MotorHAT.BACKWARD)
        
    time.sleep(2)
    myMotor.run(Adafruit_MotorHAT.RELEASE);