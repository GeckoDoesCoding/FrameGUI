#include <Servo.h>

Servo rollServo;
Servo pitchServo;

void setup() {
  Serial.begin(9600);
  
  rollServo.attach(9);  // Attach the roll servo to pin 9
  pitchServo.attach(10); // Attach the pitch servo to pin 10
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming data
    String data = Serial.readStringUntil('\n');
    
    // Parse the received data
    int roll_index = data.indexOf("Roll:");
    int pitch_index = data.indexOf("Pitch:");
    
    if (roll_index != -1 && pitch_index != -1) {
      // Extract roll and pitch values
      String roll_str = data.substring(roll_index + 5, pitch_index);
      String pitch_str = data.substring(pitch_index + 6);
      
      int roll_value = roll_str.toInt();
      int pitch_value = pitch_str.toInt();
      
      // Map the values to servo angles (adjust the mapping based on your servo's range)
      int roll_angle = map(roll_value, 0, 20, 0, 180);
      int pitch_angle = map(pitch_value, 0, 20, 0, 180);
      
      // Move the servos to the calculated angles
      rollServo.write(roll_angle);
      pitchServo.write(pitch_angle);
    }
  }
}
