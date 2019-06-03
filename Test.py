from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)  # Establish the connection on a specific port

counter = 30
ser.flush()
ser.read()
ser.read()
ser.read()
ser.read()
ser.read()
ser.read()
ser.read()
while counter<127:
     buffer=''
     counter+=1
     string = chr(counter)
     string = string.encode('ascii')
     ser.write(string)
     string = ser.read()
     string = string.decode('utf-8')
     print(string)
     buffer = buffer + string
print(buffer)


