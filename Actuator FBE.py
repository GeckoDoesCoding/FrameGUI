import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import serial

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        #self.serial_port = serial.Serial('COM5', 9600)  # Update with the correct port

        # Setting title
        self.setWindowTitle("Arduino Control")

        # Setting geometry
        self.setGeometry(300, 300, 300, 150)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        layout = QVBoxLayout(self)

        # Forward button
        forward_button = QPushButton("Forward", self)
        forward_button.clicked.connect(lambda: self.send_command("forward"))
        layout.addWidget(forward_button)

        # Backward button
        backward_button = QPushButton("Backward", self)
        backward_button.clicked.connect(lambda: self.send_command("backward"))
        layout.addWidget(backward_button)

        # Stop button
        stop_button = QPushButton("Stop", self)
        stop_button.clicked.connect(lambda: self.send_command("stop"))
        layout.addWidget(stop_button)

    def send_command(self, command):
        #Send the command to Arduino
        arduino_command = f"{command}\n"
        #self.serial_port.write(arduino_command.encode())

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
