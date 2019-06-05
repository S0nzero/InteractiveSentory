import serial as s

ser = s.Serial('/dev/ttyACM1', 9600)
while True:
    string = ser.read()
    string = string.decode('utf-8')
    print(string)

