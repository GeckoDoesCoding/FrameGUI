byte Speed = 0; // Intialize Variable for the speed of the motor (0-255);
int RPWM = 10;  // Connect Arduino pin 10 to IBT-2 pin RPWM
int LPWM = 11;  // Connect Arduino pin 11 to IBT-2 pin LPWM

void setup() {
    pinMode(10, OUTPUT); // Configure pin 10 as an Output
    pinMode(11, OUTPUT); // Configure pin 11 as an Output

    // Stop Actuator initially
    analogWrite(RPWM, 0);
    analogWrite(LPWM, 0);
}

void loop() {
    // Check for commands from serial
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        
        if (command == "Forward") {
            // Extend Actuator at Full Speed
            Speed = 255;
            analogWrite(RPWM, 0);
            analogWrite(LPWM, Speed);
        } else if (command == "Backward") {
            // Retract Actuator at Full Speed
            Speed = 255;
            analogWrite(RPWM, Speed);
            analogWrite(LPWM, 0);
        } else if (command == "Stop") {
            // Stop Actuator
            analogWrite(RPWM, 0);
            analogWrite(LPWM, 0);
        }
    }
}
