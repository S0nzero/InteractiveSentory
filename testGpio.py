import RPi.GPIO as GPIO


def hitDetected():
    return False


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
while True:
    if hitDetected():
        GPIO.output(3, GPIO.HIGH)

