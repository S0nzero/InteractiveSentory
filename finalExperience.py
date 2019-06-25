import hitDetection
import serial as s
import time
import RPi.GPIO as GPIO


def read_and_format(ser):
    result = ser.readline().decode('utf-8')
    result = result.split("/")
    result[-1] = result[-1][:-2]
    return result


def send_gpio_signal():
    print("Hit Detected on sending GPIO signal")
    GPIO.output(5, 1)
    time.sleep(0.1)
    GPIO.output(5, 0)
    time.sleep(0.1)


def checkresultformat(result, nb_sensors):
    if len(result) != nb_sensors:
        return False
    for i in result:
        if not(i.isdigit()):
            return False
    return True


def procedure():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.OUT)
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
        result = read_and_format(ser)
        if checkresultformat(result, nb_sensors):
            if hdm.new_value(result):
                print("coucou")
                send_gpio_signal()
            else:
                print("No Hit detected")
        else:
            print("Nope, problem with data")
        hdm.print_values()


procedure()
