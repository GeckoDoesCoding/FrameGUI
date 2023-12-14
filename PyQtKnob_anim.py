import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QComboBox
from PyQt6.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        # self.serial_port = serial.Serial('COM3', 9600, timeout=1)  # Update with the correct port

        # Setting title
        self.setWindowTitle("RP Adjust")

        # Setting geometry
        self.setGeometry(300, 300, 550, 250)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        # Create a central widget to hold the layouts
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set up the main layout
        main_layout = QVBoxLayout(central_widget)

        # Set up a frame for Roll and Pitch control
        roll_pitch_frame = QFrame(self)
        roll_pitch_frame.setFrameShape(QFrame.Shape.Box)
        roll_pitch_frame.setFrameShadow(QFrame.Shadow.Raised)
        roll_pitch_frame.setLineWidth(2)

        # Set up Roll and Pitch layout inside the frame
        roll_pitch_layout = QHBoxLayout(roll_pitch_frame)

        # Set up Roll dial
        roll_dial = QDial(self)
        roll_dial.setRange(0, 20)
        roll_dial.setGeometry(100, 175, 75, 75)
        roll_dial.setNotchesVisible(True)
        roll_dial_value_label = QLabel("Roll value is: 0", self)
        roll_dial_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        roll_dial.valueChanged.connect(lambda value: self.update_label_and_send("Roll", value, roll_dial_value_label))
        roll_pitch_layout.addWidget(roll_dial)
        roll_pitch_layout.addWidget(roll_dial_value_label)

        # Set up Pitch dial
        pitch_dial = QDial(self)
        pitch_dial.setRange(0, 20)
        pitch_dial.setGeometry(400, 175, 75, 75)
        pitch_dial.setNotchesVisible(True)
        pitch_dial_value_label = QLabel("Pitch value is: 0", self)
        pitch_dial_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pitch_dial.valueChanged.connect(lambda value: self.update_label_and_send("Pitch", value, pitch_dial_value_label))
        roll_pitch_layout.addWidget(pitch_dial)
        roll_pitch_layout.addWidget(pitch_dial_value_label)

        # Set the title of the frame
        roll_pitch_frame.setObjectName("RollPitchFrame")

        # Add Roll and Pitch layout to the main layout
        main_layout.addWidget(roll_pitch_frame)

        # Set up a frame for Port Configuration
        port_config_frame = QFrame(self)
        port_config_frame.setFrameShape(QFrame.Shape.Box)
        port_config_frame.setFrameShadow(QFrame.Shadow.Raised)
        port_config_frame.setLineWidth(2)

        # Set up Port Configuration layout inside the frame
        port_config_layout = QVBoxLayout(port_config_frame)

        # Set up COM port selection
        com_label = QLabel("Select COM Port:", self)
        com_combobox = QComboBox(self)
        com_combobox.setFixedWidth(200)
        com_combobox.addItems([f"COM{i}" for i in range(1, 19)])

        # Add COM port selection to the layout
        port_config_layout.addWidget(com_label)
        port_config_layout.addWidget(com_combobox)

        # Set the title of the frame
        port_config_frame.setObjectName("PortConfigFrame")

        # Add Port Configuration layout to the main layout
        main_layout.addWidget(port_config_frame)

    def update_label_and_send(self, parameter, value, label):
        # Send the parameter and value to Arduino
        # message = f"{parameter}:{value}\n"
        # self.serial_port.write(message.encode())
        label.setText(f"{parameter} value is: {value}")

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
