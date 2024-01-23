#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;
const int MPU_addr=0x68;
byte Speed = 0;
const int RPWM = 10; // connect Arduino pin 10 to IBT-2 pin RPWM
const int LPWM = 11; // connect Arduino pin 11 to IBT-2 pin LPWM

int16_t axis_X, axis_Y, axis_Z;
int minVal = 265;
int maxVal = 402;
double x, y, z;

void setup() {
  pinMode(10, OUTPUT); // Configure pin 10 as an Output
  pinMode(11, OUTPUT); // Configure pin 11 as an Output

  // Stop Actuator initially
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);

  // Start serial communication
  Serial.begin(9600);

  // Initialize MPU6050
  Wire.begin();
  Wire.beginTransmission(0x68);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
}

void ReadMPUData()
{
  Wire.beginTransmission(0x68);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(0x68, 14, true);
  axis_X = Wire.read() << 8 | Wire.read();
  axis_Y = Wire.read() << 8 | Wire.read();
  axis_Z = Wire.read() << 8 | Wire.read();

  int xAng = axis_X;
  int yAng = axis_Y;
  int zAng = axis_Z;

  x = RAD_TO_DEG * (atan2(-yAng, -zAng) + PI);
  y = RAD_TO_DEG * (atan2(-xAng, -zAng) + PI);
  z = RAD_TO_DEG * (atan2(-yAng, -xAng) + PI);

  Serial.print(x);
  Serial.print(", ");
  Serial.println(y);
}

void loop() {
  // Read data from MPU6050
 
  //ReadMPUData();
  
  // Linear actuator control logic based on pitch angle
  if (Serial.available() > 0) {
    // Read the incoming command
    char command = Serial.read();

    // Execute the corresponding action based on the command
    switch (command) {
      case 'R':
        // Read MPU Data
        ReadMPUData();
        break;

      case 'F':
        // Forward
        Speed = 255;
        analogWrite(RPWM, 0);
        analogWrite(LPWM, Speed);
        ReadMPUData();
        break;

      case 'B':
        // Backward
        Speed = 255;
        analogWrite(RPWM, Speed);
        analogWrite(LPWM, 0);
        ReadMPUData();
        break;

      case 'S':
        // Stop
        analogWrite(RPWM, 0);
        analogWrite(LPWM, 0);
        ReadMPUData();
        break;

      // Add more cases for other commands if needed
      default:
        // Invalid command
        break;
         }
}
}