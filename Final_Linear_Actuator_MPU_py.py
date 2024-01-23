import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
import serial

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        self.serial_port = serial.Serial('COM5', 9600)

        self.setWindowTitle("Magna_Test_Bench_Automation")
        self.setGeometry(400, 400, 400, 200)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        read_button = QPushButton("Read MPU Data", self)
        read_button.clicked.connect(lambda: self.send_command_to_arduino("R"))
        main_layout.addWidget(read_button)

        forward_button = QPushButton("Forward", self)
        forward_button.clicked.connect(lambda: self.send_command_to_arduino("F"))
        main_layout.addWidget(forward_button)

        backward_button = QPushButton("Backward", self)
        backward_button.clicked.connect(lambda: self.send_command_to_arduino("B"))
        main_layout.addWidget(backward_button)

        stop_button = QPushButton("Stop", self)
        stop_button.clicked.connect(lambda: self.send_command_to_arduino("S"))
        main_layout.addWidget(stop_button)
        
          # MPU6050 Data Display
        self.mpu_label = QLabel("Roll & Pitch Data:\nRoll: N/A\nPitch: N/A", self)
        main_layout.addWidget(self.mpu_label)
    
    def read_data(self):
        try:
            # Read data from Arduino for MPU6050
            mpu_data = self.serial_port.readline().decode().strip().split(',')
            x_value, y_value = mpu_data[0], mpu_data[1]
            print(x_value, y_value)

            # Update MPU6050 label
            self.mpu_label.setText(f"MPU6050 Data:\nX: {x_value}\nY: {y_value}")
            print(x_value, y_value)

        except Exception as e:
            print(f"Error reading data: {e}")


    def send_command_to_arduino(self, command):
        # Send command to Arduino (F for Forward, B for Backward, S for Stop)
        self.serial_port.write(f"{command}\n".encode())

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
