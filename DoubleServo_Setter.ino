
Servo RollServo;
Servo PitchServo;

void setup() {
  Serial.begin(9600);
  
  RollServo.attach(9);// Assuming the servo is connected to pin 9
  PitchServo.attach(10);
  
  RollServo.write(0);
  PitchServo.write(0);
}

void loop() {
  
  if (Serial.available() > 3)
   {
    int roll = Serial.parseInt();
    int pitch = Serial.parseInt();
    int roll_pin = Serial.parseInt();
    int pitch_pin = Serial.parseInt();
    
    int r = RollServo.read();
    int p = PitchServo.read();
 
    delay(1000);

    for (int pos = r; pos <= roll; pos += 1) 
    { 
       delay(1000); // goes from 0 degrees to 180 degrees
       RollServo.write(pos);              // tell servo to go to position in variable 'pos' 
    }
    RollServo.detach();

    for (int pos = p; pos <= roll; pos += 1) 
    { 
       delay(1000); // goes from 0 degrees to 180 degrees
       PitchServo.write(pos);              // tell servo to go to position in variable 'pos' 
    }
    PitchServo.detach();
    
    Serial.flush();  // Clear the serial buffer
  }
}
