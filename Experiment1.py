import serial as s
import time
import csv


def main_procedure():
    type_tested = input("Enter the type of experiment: ")
    csv_writer([type_tested])
    l = []
    counter = 0
    timeout = time.time()+5
    while time.time() < timeout:
        ser = s.Serial('/dev/ttyACM1', 9600)
        string = ser.readline().decode('utf-8')
        print(string)
        if counter >= 1:
            l.append(int(string[0:-2]))
        else:
            counter += 1
    csv_writer(l)


def csv_writer(l):
    with open("./results/resultsExperiment1.csv", 'a') as csvfile:
        wr = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(l)


name = input("Enter the name of the participant: ")
csv_writer([name])
main_procedure()
for i in range(2):
    input("Press Enter to continue the experience !")
    main_procedure()
print("Thanks a lot !")
time.sleep(3)
