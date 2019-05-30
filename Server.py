import serial as s

ser = s.Serial('/dev/ttyACM0', 9600)
while True:
    string = ser.read()
    string = string.decode('utf-8')
    if (string =='1'):
        print("Yay! :)")
    else:
        print("Nay :(")


