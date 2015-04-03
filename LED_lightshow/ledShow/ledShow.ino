const int ledPin = 13; // the pin that the LED is attached to
int incomingData;      // a variable to read incoming serial data into

void setup() {
  // initialise serial communication:
  Serial.begin(9600);
  // initialise the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // check if there is incoming serial data
  if (Serial.available() > 0) {
    
    incomingData = Serial.read();
    // if it's a capital S, turn on the LED:
    if (incomingData == 'S') {
      digitalWrite(ledPin, HIGH);
    } 
    // if it's a D, turn off the LED:
    if (incomingData == 'D') {
      digitalWrite(ledPin, LOW);
    }
  }
}
