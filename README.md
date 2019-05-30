# InteractiveSentory
A github to make the Sentory device interactive

##Requirements
The Serial library is necessary https://pythonhosted.org/pyserial/pyserial.html#overview
Create your venv with this library and that's it !
Python 3.6 is used

## How to make it work
First, make the arduino execute the little piece of code provided
    
It makes the Arduino send back the data sent through the serial port
    
Then, execute the Server.py script as root. This script waits for data to be provided and checks if a 1 was sent or not

Finally, execute Client.py which is going to sent a 1, and then a 2
You should get a Yay! and a Nay !, which shows that it works basically !

