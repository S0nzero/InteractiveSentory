import serial as s
import time
import csv
import os


def main_procedure():
    counter = 0
    results_list=[]
    nb_sensors = ''
    while not(nb_sensors.isdigit()):
        if counter != 0:
            print("Please input a number")
        else:
            counter += 1
        nb_sensors = input("Input the number of sensors tested: ")
    nb_sensors = int(nb_sensors)
    name = input("Please enter the name of the participant: ")
    csv_writer([name])
    counter = 0
    for i in range(nb_sensors):
        results_list.append([])
    print(results_list)
    for i in range(10):
        input("Ready for the next test? Press enter then!")
        timeout = time.time()+3
        while time.time() < timeout:
            ser = s.Serial('/dev/ttyACM1', 9600)
            result = ser.readline().decode('utf-8').split('/', 1)
            print(result)
            if counter == 0:
                results_list[int(result[0])].append(int(result[1][0:-2]))
            else:
                counter += 1
    for i in range(len(results_list)):
        results_list[i].insert(0, i)
        csv_writer(results_list[i])
    print(results_list)


def csv_writer(l):
    try:
        with open("./results/resultsExperiment2.csv", 'a') as csvfile:
            wr = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(l)
    except IOError:
        print("File doesn't exist. Creating file...")
        try:
            os.mkdir("./results")
        except Exception:
            pass
        csv_writer(l)

main_procedure()
