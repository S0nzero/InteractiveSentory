import serial as s
ser = s.Serial('/dev/ttyACM0', 9600)
string = "1"
string = string.encode('ascii')
ser.write(string)
string = "2"
string = string.encode('ascii')
ser.write(string)