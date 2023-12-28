byte Speed = 0; // Initialize Variable for the speed of the motor (0-255);
int RPWM = 10;  // Connect Arduino pin 10 to IBT-2 pin RPWM
int LPWM = 11;  // Connect Arduino pin 11 to IBT-2 pin LPWM

void setup() {
  pinMode(10, OUTPUT); // Configure pin 10 as an Output
  pinMode(11, OUTPUT); // Configure pin 11 as an Output

  // Stop Actuator initially
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);

  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if there is data available to read
  if (Serial.available() > 0) {
    // Read the incoming command
    char command = Serial.read();

    // Execute the corresponding action based on the command
    switch (command) {
      case 'F':
        // Forward
        Speed = 255;
        analogWrite(RPWM, 0);
        analogWrite(LPWM, Speed);
        break;

      case 'B':
        // Backward
        Speed = 255;
        analogWrite(RPWM, Speed);
        analogWrite(LPWM, 0);
        break;

      case 'S':
        // Stop
        analogWrite(RPWM, 0);
        analogWrite(LPWM, 0);
        break;

      // Add more cases for other commands if needed

      default:
        // Invalid command
        break;
    }
  }
}
