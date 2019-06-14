const int ledPin = 13;      // LED connected to digital pin 13
const int knockSensor0 = A0; // the piezo is connected to analog pin 0
const int knockSensor1 = A1; // the piezo is connected to analog pin 0
const int threshold = 0; 

int sensorReading0 = 0; // variable to store the value read from the sensor pin
int sensorReading1 = 1; // variable to store the value read from the sensor pin
int ledState = LOW; 

void setup() {
  Serial.begin(9600);
}

void loop() {
    sensorReading0 = analogRead(knockSensor0);
    sensorReading1 = analogRead(knockSensor1);
  
    if (sensorReading0 >= threshold && sensorReading1 < threshold) {
      Serial.println(String("0/")+sensorReading0);
      delay(100);
    }
      
    else if (sensorReading0 >= threshold && sensorReading1 >= threshold) {
      // toggle the status of the ledPin:
      if(sensorReading0 > sensorReading1){
        Serial.println(String("0/")+sensorReading0);
        delay(100);
      }
      else{
        Serial.println(String("1/")+sensorReading1);
        delay(100);
      }
    }
    
    else if(sensorReading0 < threshold && sensorReading1 >= threshold){
      Serial.println(String("1/")+sensorReading1);
        delay(100);
    }
}
