import hitDetection
import serial as s
import time
import csv
import os
import RPi.GPIO


def procedure():
    hitDetector = hitDetection.HitDetector
    counter=0
    ser = s.Serial('/dev/ttyACM1', 9600)
    result = ser.readline().decode('utf-8').split('/', 1)
    print(result)
    if counter == 0:
        if hitDetector.new_value(new=int(result[1])):
            print("Knock!!")
            #TODO Implement the gpio change here
    else:
        counter += 1