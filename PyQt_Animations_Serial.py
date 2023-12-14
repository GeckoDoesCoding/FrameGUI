import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *
import serial

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        self.serial_port = serial.Serial('COM6', 9600, timeout=1)  # Update with the correct port

        # Setting title
        self.setWindowTitle("RP Adjust")
        #self.setWindowIcon(QtGui.QIcon('C:/users/shoukulk/Desktop/work/pics/MagnaLogo.png'))

        # Setting geometry
        self.setGeometry(300, 300, 550, 250)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        dial = QDial(self)
        dial.setGeometry(50, 50, 150, 150)
        dial.setRange(0, 20)
        dial.setNotchesVisible(True)

        label = QLabel("Set Roll", self)
        label.setGeometry(100, 175, 75, 75)
        label.setWordWrap(True)
        dial.valueChanged.connect(lambda: self.update_label_and_send("Roll", dial.value()))
        dial.valueChanged.connect(lambda: label.setText("Roll is: \n" + str(dial.value()) + " Deg"))

        dial2 = QDial(self)
        dial2.setGeometry(350, 50, 150, 150)
        dial2.setRange(0, 20)
        dial2.setNotchesVisible(True)

        label2 = QLabel("Set Pitch", self)
        label2.setGeometry(400, 175, 75, 75)
        label2.setWordWrap(True)
        dial2.valueChanged.connect(lambda: self.update_label_and_send("Pitch", dial2.value()))
        dial2.valueChanged.connect(lambda: label2.setText("Pitch is: \n" + str(dial2.value()) + " Deg"))

    def update_label_and_send(self, parameter, value):
        label_text = f"{parameter} is:\n{value} Deg"
        label.setText(label_text)

        # Send the parameter and value to Arduino
        message = f"{parameter}:{value}\n"
        self.serial_port.write(message.encode())

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
