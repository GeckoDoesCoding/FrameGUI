byte Speed = 0; // Initialize variable for the speed of the motor (0-255);
int RPWM = 10;  // Connect Arduino pin 10 to IBT-2 pin RPWM
int LPWM = 11;  // Connect Arduino pin 11 to IBT-2 pin LPWM


void setup() {
  pinMode(10, OUTPUT); // Configure pin 10 as an Output
  pinMode(11, OUTPUT); // Configure pin 11 as an Output
  pinMode(actuatorPin, OUTPUT); // Configure actuator control pin as an Output

  // Initial position - Stop Actuator
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);
  digitalWrite(actuatorPin, LOW);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    switch (command) {
      case 'F':
        // Forward
        moveActuator(255);
        break;
      case 'B':
        // Backward
        moveActuator(-255);
        break;
      case 'S':
        // Stop
        stopActuator();
        break;
      case 'P':
        // Move by Pitch
        moveByPitch();
        break;
      default:
        break;
    }
  }
}

void moveActuator(int speed) {
  Speed = constrain(speed, -255, 255);

  // Extend Actuator
  analogWrite(RPWM, 0);
  analogWrite(LPWM, Speed);

  delay(2000); // 2 Seconds
  
  // Stop Actuator
  stopActuator();

  delay(2000); // 2 Seconds
}

void stopActuator() {
  // Stop Actuator
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);
  digitalWrite(actuatorPin, LOW);

  delay(2000); // 2 Seconds
}

void moveByPitch() {
  int pitchValue = Serial.parseInt();
  int delayTime = pitchValue * 1000;

  // Extend Actuator
  moveActuator(255);

  delay(delayTime);

  // Stop Actuator
  stopActuator();
}
