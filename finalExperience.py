import hitDetection
import serial as s
import time
import csv
import os
# import RPi.GPIO as GPIO


def procedure():
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(5, GPIO.OUT)
    counter = 0
    nb_sensors = ''
    while not (nb_sensors.isdigit()):
        if counter != 0:
            print("Please input a number")
        else:
            counter += 1
        nb_sensors = input("Input the number of sensors tested: ")
    nb_sensors = int(nb_sensors)
    hdm = hitDetection.HitDetectorManager(nb_sensors, 50, 15)
    while True:
        ser = s.Serial('/dev/ttyACM0', 9600)
        result = ser.readline().decode('utf-8').split('/', 1)
        if len(result) == 2:
            sensor = result[0]
            resultofsensor = result[1][:-2]
            print(sensor, result[1])
            if (sensor.isdigit()) and (resultofsensor.isdigit()):
                if hdm.new_value(result):
                    print("Hit Detected on "+result[0]+", sending GPIO signal")
                    # GPIO.output(5, 1)
                    # time.sleep(0.5)
                    # GPIO.output(5, 0)
                    # time.sleep(0.5)
                else:
                    print("No Hit detected")
            else:
                print("Nope")
        else:
            print("Nope")


procedure()
