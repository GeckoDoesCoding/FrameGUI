#include <Servo.h>

Servo rollServo;
Servo pitchServo;

void setup() {
  Serial.begin(9600);

  // Attach servos to the corresponding pins
  rollServo.attach(9);   // Update with the correct pin for the roll servo
  pitchServo.attach(10);  // Update with the correct pin for the pitch servo
}

void loop() {
  if (Serial.available() > 0) {
    // Read the message from serial
    String message = Serial.readStringUntil('\n');

    // Extract parameter and value from the message
    String parameter = message.substring(0, message.indexOf(':'));
    int value = message.substring(message.indexOf(':') + 1).toInt();

    // Adjust servo motors based on the parameter and value
    if (parameter == "Roll") {
      setRollAngle(value);
    } else if (parameter == "Pitch") {
      setPitchAngle(value);
    }
  }
}

void setRollAngle(int angle) {
  // Adjust the roll servo angle
  rollServo.write(angle);
  delay(15);  // Add a small delay for smooth operation
}

void setPitchAngle(int angle) {
  // Adjust the pitch servo angle
  pitchServo.write(angle);
  delay(15);  // Add a small delay for smooth operation
}
