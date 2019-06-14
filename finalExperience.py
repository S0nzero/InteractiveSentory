import hitDetection
import serial as s
import time
import csv
import os


def procedure():
    hit_detector0 = hitDetection.HitDetector(50, 15)
    hit_detector1 = hitDetection.HitDetector(50, 15)
    while True:
        counter = 0
        ser = s.Serial('/dev/ttyACM0', 9600)
        result = ser.readline().decode('utf-8').split('/', 1)
        if counter == 0:
            if result[0] == '0':
                if hit_detector0.new_value(new=int(result[1])):
                    print("Knock!! Sensor was: ", result[0], "Value was: ", result[1])
                    # TODO Implement the gpio change here
            if result[0] == '1':
                if hit_detector1.new_value(new=int(result[1])):
                    print("Knock!! Sensor was: ", result[0], "Value was: ", result[1])
                    # TODO Implement the gpio change here
            else:
                counter += 1


procedure()