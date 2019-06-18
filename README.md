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
- If the computing tells us that a hit was detected, we send a GPIO input to the brightsigns to update the presentation

##Code Explanation

###HitDetectorManager class

This class is simply useful for the user: There's no need anymore to manually create the HitDetectors, everything
is handled by this class. The constructor takes the number of sensors in parameter

Everytime a new value is sent by the Arduino, we give the result to the function new_value, which redirects the result 
to the right HitDetector object

###HitDetector class

This class aims to compute the values sent by the sensors, in order to detect when there's a hit on a sensor. To do so,
we use the following method:
For every value sent by the arduino:

a,b,c,d are constants that are imutable in the beginning of the execution

If there's less than a values: We store the new value
If there's between b and c values: We check if the value is bigger than the confidence interval [1]
- If it is: We flush the list and send a GPIO signal to the brightsign to change its state
- Otherwise: We add the value to the list and continue

If there c values in the list, and what was recieved isn't a hit, we pop the head of the list and add the new value 
to the list



[1] The Confidence interval is (AVG-SD - d, AVG+SD + d)

###finalExperience.py

This file is the main of the project. Basically:
- Ask the user how much sensors are used (Useful for testing)
- Create a hitDetectorManager that will be used throughout the experiment.
- Recieve the data
- Compute it with HitDetectorManager



