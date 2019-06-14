# InteractiveSentory
A github to make the Sentory device interactive

##Requirements

- Python 3.6 
- Serialg
- Scipy
- RPI.GPIO 

## How to make it work

Every script should be executed as root, since we read system serial files

Don't forget to install the required dependencies



## How does it work

The code enables the user to detect the hits made on piezo sensors, by reading the serial port data from an Arduino and
computing it. Basically, the following steps happen:
- At a given time, the Arduino computes the biggest value out of all sensors, and sends it through the serial port
- Python gets this data and updates the past data it had in a hitDetector object

####HitDetector class
- A list of the previous past values is kept in memory
- Thanks to the values in this list, everytime a new value is sent, we compute the confidence interval, to determine
whether or not the new value should be considered as a hit or not
- If not: The value is added and the first value is popped out of the list
- Otherwise, we flush the data and tell the BrightSign that a hit was detected



