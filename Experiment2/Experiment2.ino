const int threshold = 0;

// Add enough variables for every sensor plugged in the arduino.
const int knockSensor0 = A0;
const int knockSensor1 = A1;
int sensorReading0 = 0;
int sensorReading1 = 0;
int ledState = LOW; 

void setup() {
  Serial.begin(9600);
}

void loop() {
    // Add enough lines for every sensor plugged in the Arduino
    sensorReading0 = analogRead(knockSensor0);
    sensorReading1 = analogRead(knockSensor1);
    Serial.println(sensorReading0+String("/")+sensorReading1);   
    delay(100);
}
