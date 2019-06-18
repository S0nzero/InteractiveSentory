import hitDetection
import serial as s
import time
import csv
import os


def procedure():
    counter = 0
    nb_sensors = ''
    while not (nb_sensors.isdigit()):
        if counter != 0:
            print("Please input a number")
        else:
            counter += 1
        nb_sensors = input("Input the number of sensors tested: ")
    nb_sensors = int(nb_sensors)
    counter = 0
    hdm = hitDetection.HitDetectorManager(nb_sensors, 50, 15)
    while True:
        ser = s.Serial('/dev/ttyACM0', 9600)
        result = ser.readline().decode('utf-8').split('/', 1)
        if counter != 0:
            if hdm.new_value(result):
                print("Hit Detected on "+result[0]+", sending GPIO signal")

            else:
                print("No Hit detected")
        else:
            counter += 1


procedure()