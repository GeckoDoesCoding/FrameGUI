import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial, QLabel, QVBoxLayout, QWidget, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *
import serial

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        self.serial_port = serial.Serial('COM16', 9600, timeout=1)  # Update with the correct port

        # Setting title
        self.setWindowTitle("RP Adjust")
        self.setWindowIcon(QtGui.QIcon('C:/Users/Mohit Kolte/Desktop/magna/mitwpu.jpg'))

        # Setting geometry
        self.setGeometry(300, 300, 750, 350)
        self.setStyleSheet("background-color: #030303;")
        self.UiComponents()
        self.show()

    def UiComponents(self):
        main_frame = QFrame(self)
        main_frame.setGeometry(50, 50, 650, 250)
        main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        main_frame.setFrameShadow(QFrame.Shadow.Raised)
        main_frame.setLineWidth(2)

        main_layout = QHBoxLayout(main_frame)

        # Dials Frame
        dials_frame = QFrame(self)
        dials_frame.setFrameShape(QFrame.Shape.StyledPanel)
        dials_frame.setLineWidth(5)
        dials_frame.setStyleSheet("background-color: #ebf1f5;")

        dials_layout = QHBoxLayout(dials_frame)

        dial = QDial(self)
        dial.setFixedSize(150, 150)
        dial.setGeometry(50, 50, 150, 150)
        dial.setRange(0, 20)
        dial.setNotchesVisible(True)

        label = QLabel("Set Roll", self)
        label.setWordWrap(True)
        dial.valueChanged.connect(lambda: self.update_label_and_send("Roll", dial.value()))
        dial.valueChanged.connect(lambda: label.setText("Roll is: \n" + str(dial.value()) + " Deg"))

        dial2 = QDial(self)
        dial2.setFixedSize(150, 150)
        dial2.setGeometry(350, 50, 150, 150)
        dial2.setRange(0, 23)
        dial2.setNotchesVisible(True)

        label2 = QLabel("Set Pitch", self)
        label2.setWordWrap(True)
        dial2.valueChanged.connect(lambda: self.update_label_and_send("Pitch", dial2.value()))
        dial2.valueChanged.connect(lambda: label2.setText("Pitch is: \n" + str(dial2.value()) + " Deg"))

        dials_layout.addWidget(dial)
        dials_layout.addWidget(label)
        dials_layout.addWidget(dial2)
        dials_layout.addWidget(label2)

        main_layout.addWidget(dials_frame)

        # Sensor Data Frame
        sensor_data_frame = QFrame(self)
        sensor_data_frame.setGeometry(550, 50, 200, 150)
        sensor_data_frame.setFrameShape(QFrame.Shape.Box)
        sensor_data_frame.setFrameShadow(QFrame.Shadow.Raised)
        sensor_data_frame.setLineWidth(2)

        sensor_data_layout = QVBoxLayout(sensor_data_frame)

        self.roll_sensor_label = QLabel("Roll Sensor: 0", self)
        self.pitch_sensor_label = QLabel("Pitch Sensor: 0", self)

        sensor_data_layout.addWidget(self.roll_sensor_label)
        sensor_data_layout.addWidget(self.pitch_sensor_label)
        sensor_data_frame.setStyleSheet("background-color: #ebf1f5;")

        main_layout.addWidget(sensor_data_frame)

        # Status Frame
        status_frame = QFrame(self)
        status_frame.setFrameShape(QFrame.Shape.StyledPanel)
        status_frame.setLineWidth(5)
        status_frame.setStyleSheet("background-color: #ebf1f5;")

        status_layout = QVBoxLayout(status_frame)

        color_label = QLabel("Status", self)
        color_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_layout.addWidget(color_label)

        self.color_window = QFrame(self)
        self.color_window.setStyleSheet("background-color: green;")
        status_layout.addWidget(self.color_window)

        main_layout.addWidget(status_frame)

    def update_label_and_send(self, parameter, value):
        label_text = f"{parameter} is:\n{value} Deg"

        # Send the parameter and value to Arduino
        message = f"{parameter}:{value}\n"
        self.serial_port.write(message.encode())

        # Update Sensor Data Frame
        self.roll_sensor_label.setText(f"Roll Sensor: {value * 0.94:.2f}")
        self.pitch_sensor_label.setText(f"Pitch Sensor: {value * 1.06:.2f}")

        # Update Status Frame
        if parameter == "Pitch" and value > 21:
            self.color_window.setStyleSheet("background-color: red;")
        else:
            self.color_window.setStyleSheet("background-color: green;")

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
