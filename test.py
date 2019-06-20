import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
for i in range(16):
    print("coucou")
    GPIO.output(5,1)
    time.sleep(0.5)
    GPIO.output(5,0)
    time.sleep(0.5)
GPIO.cleanup()
print("cleanup")
