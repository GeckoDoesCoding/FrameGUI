import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import serial

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        self.serial_port = serial.Serial('COM5', 9600)

        self.setWindowTitle("Actuator Control")
        self.setGeometry(300, 300, 300, 150)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        forward_button = QPushButton("Forward", self)
        forward_button.clicked.connect(lambda: self.send_command_to_arduino('F'))
        main_layout.addWidget(forward_button)

        backward_button = QPushButton("Backward", self)
        backward_button.clicked.connect(lambda: self.send_command_to_arduino('B'))
        main_layout.addWidget(backward_button)

        stop_button = QPushButton("Stop", self)
        stop_button.clicked.connect(lambda: self.send_command_to_arduino('S'))
        main_layout.addWidget(stop_button)

    def send_command_to_arduino(self, command):
        # Send the command to Arduino
        self.serial_port.write(command.encode())

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
