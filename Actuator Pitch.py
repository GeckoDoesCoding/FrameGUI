import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget
import serial

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        self.serial_port = serial.Serial('COM5', 9600)

        self.setWindowTitle("Actuator Control")
        self.setGeometry(300, 300, 300, 200)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        pitch_label = QLineEdit(self)
        pitch_label.setPlaceholderText("Enter Pitch Angle")
        main_layout.addWidget(pitch_label)

        move_pitch_button = QPushButton("Move by Pitch", self)
        move_pitch_button.clicked.connect(lambda: self.send_pitch_to_arduino(pitch_label.text()))
        main_layout.addWidget(move_pitch_button)

        forward_button = QPushButton("Forward", self)
        forward_button.clicked.connect(lambda: self.send_command_to_arduino("F"))
        main_layout.addWidget(forward_button)

        backward_button = QPushButton("Backward", self)
        backward_button.clicked.connect(lambda: self.send_command_to_arduino("B"))
        main_layout.addWidget(backward_button)

        stop_button = QPushButton("Stop", self)
        stop_button.clicked.connect(lambda: self.send_command_to_arduino("S"))
        main_layout.addWidget(stop_button)

    def send_pitch_to_arduino(self, pitch_angle):
        try:
            # Convert pitch angle to an integer
            pitch = int(float(pitch_angle))

            # Check if pitch is within a valid range
            if 0 <= pitch <= 20:
                # Send pitch value to Arduino
                self.serial_port.write(f"P{pitch}\n".encode())
            else:
                print("Pitch angle must be between 0 and 20 degrees.")
        except ValueError:
            print("Invalid pitch angle. Please enter a numeric value.")

    def send_command_to_arduino(self, command):
        # Send command to Arduino (F for Forward, B for Backward, S for Stop)
        self.serial_port.write(f"{command}\n".encode())

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
