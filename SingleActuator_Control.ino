byte Speed = 0; // Initialize Variable for the speed of the motor (0-255)
int RPWM = 10;  // Connect Arduino pin 11 to IBT-2 pin LPWM
int LPWM = 11;

void setup() {
  pinMode(10, OUTPUT); // Configure pin 11 as an Output
  pinMode(11, OUTPUT);
}

void loop() {
  // Read the value sent from GUI for pitch 
  int pitchDelay = Serial.parseInt();

  // Extend Actuator
  Speed = 255;
analogWrite(LPWM, Speed);
analogWrite(RPWM, 0); 
  // Retract Actuator
analogWrite(LPWM, 0);
analogWrite(RPWM, Speed);

  delay(pitchDelay); // Extending for the time period given by the user

  // Stop Actuator
  analogWrite(LPWM, 0);
  analogWrite(RPWM, 0);
}
