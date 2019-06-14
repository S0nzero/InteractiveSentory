import hitDetection
import serial as s
import time
import csv
import os
import RPi.GPIO


def procedure():
    hit_detector = hitDetection.HitDetector(50, 15)
    counter = 0
    ser = s.Serial('/dev/ttyACM1', 9600)
    result = ser.readline().decode('utf-8').split('/', 1)
    print(result)
    if counter == 0:
        if hit_detector.new_value(new=int(result[1])):
            print("Knock!!")g
            # TODO Implement the gpio change here
    else:
        counter += 1