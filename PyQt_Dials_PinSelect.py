import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial, QLabel, QVBoxLayout, QWidget, QFrame, QComboBox, QHBoxLayout, QGridLayout
from PyQt6.QtCore import Qt
import serial

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Serial communication setup
        self.serial_port = None  # Initialize to None
        self.com_port = None
        self.roll_pin = None
        self.pitch_pin = None

        # Setting title
        self.setWindowTitle("RP Adjust")

        # Setting geometry
        self.setMinimumSize(800, 400)
        self.setStyleSheet("background-color: light blue;")
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
        rp_title = QLabel(" Set Roll and Pitch: ", self)
        rp_title.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        roll_pitch_frame.setFrameShape(QFrame.Shape.StyledPanel)
        roll_pitch_frame.setLineWidth(5)

        # Set up Roll and Pitch layout inside the frame
        roll_pitch_layout = QHBoxLayout(roll_pitch_frame)
        roll_pitch_layout.addWidget(rp_title)

        # Set up Roll dial
        roll_dial = QDial(self)
        roll_dial.setRange(0, 20)
        roll_dial.setNotchesVisible(True)
        roll_dial_value_label = QLabel("Roll value is: 0", self)
        roll_dial_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        roll_dial.valueChanged.connect(lambda value: self.update_label_and_send("Roll", value, roll_dial_value_label))
        roll_pitch_layout.addWidget(roll_dial)
        roll_pitch_layout.addWidget(roll_dial_value_label)

        # Set up Pitch dial
        pitch_dial = QDial(self)
        pitch_dial.setRange(0, 20)
        pitch_dial.setNotchesVisible(True)
        pitch_dial_value_label = QLabel("Pitch value is: 0", self)
        pitch_dial_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pitch_dial.valueChanged.connect(lambda value: self.update_label_and_send("Pitch", value, pitch_dial_value_label))
        roll_pitch_layout.addWidget(pitch_dial)
        roll_pitch_layout.addWidget(pitch_dial_value_label)

        # Add Roll and Pitch layout to the main layout
        main_layout.addWidget(roll_pitch_frame)

        # Set up a grid layout for Configuration
        config_grid_layout = QGridLayout()

        # Set up a frame for Port Configuration
        port_config_frame = QFrame(self)
        port_config_frame.setFrameShape(QFrame.Shape.Box)
        port_config_frame.setFrameShadow(QFrame.Shadow.Raised)
        port_config_frame.setLineWidth(2)

        # Set up Port Configuration layout inside the frame
        port_config_layout = QVBoxLayout(port_config_frame)

        # Set up COM port selection
        com_label = QLabel("Select COM Port:", self)
        com_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        com_combobox = QComboBox(self)
        com_combobox.addItems([f"COM{i}" for i in range(1, 19)])
        com_combobox.currentIndexChanged.connect(self.com_port_selected)

        # Add COM port selection to the layout
        port_config_layout.addWidget(com_label)
        port_config_layout.addWidget(com_combobox)

        # Set the title of the frame
        port_config_frame.setObjectName("PortConfigFrame")

        # Add Port Configuration layout to the grid layout
        config_grid_layout.addWidget(port_config_frame, 1, 2, 1, 2)

        # Set up a frame for Configuration
        config_frame = QFrame(self)
        config_frame.setFrameShape(QFrame.Shape.Box)
        config_frame.setFrameShadow(QFrame.Shadow.Raised)
        config_frame.setLineWidth(2)

        # Set up Configuration layout inside the frame
        config_layout = QHBoxLayout(config_frame)

        # Set up a horizontal layout for pin selection
        pin_selection_layout = QVBoxLayout()

        # Set up Roll Pin selection
        roll_pin_label = QLabel("Select Roll Pin:", self)
        roll_pin_combobox = QComboBox(self)
        roll_pin_combobox.setFixedWidth(150)
        roll_pin_combobox.addItems([str(i) for i in range(1, 11)])
        roll_pin_combobox.currentIndexChanged.connect(self.roll_pin_selected)

        # Set up Pitch Pin selection
        pitch_pin_label = QLabel("Select Pitch Pin:", self)
        pitch_pin_combobox = QComboBox(self)
        pitch_pin_combobox.setFixedWidth(150)
        pitch_pin_combobox.addItems([str(i) for i in range(1, 11)])
        pitch_pin_combobox.currentIndexChanged.connect(self.pitch_pin_selected)

        # Add Roll and Pitch Pin selections to the horizontal layout
        pin_selection_layout.addWidget(roll_pin_label)
        pin_selection_layout.addWidget(roll_pin_combobox)
        pin_selection_layout.addWidget(pitch_pin_label)
        pin_selection_layout.addWidget(pitch_pin_combobox)

        # Add the horizontal pin selection layout to the overall configuration layout
        config_layout.addLayout(pin_selection_layout)

        # Set the title of the frame
        config_frame.setObjectName("ConfigFrame")

        # Add Configuration layout to the grid layout
        config_grid_layout.addWidget(config_frame, 1, 0, 1, 2)

        # Add the grid layout to the main layout
        main_layout.addLayout(config_grid_layout)

    def update_label_and_send(self, parameter, value, label):
        label.setText(f"{parameter} value is: {value}")

    def com_port_selected(self, index):
        self.com_port = f"COM{index + 1}"
        print(f"Selected COM Port: {self.com_port}")

        # Initialize or update serial port with the selected COM port
        if self.serial_port:
            self.serial_port.close()

        self.serial_port = serial.Serial(self.com_port, 9600, timeout=1)
        print(f"Serial port initialized on {self.com_port}")

    def roll_pin_selected(self, index):
        self.roll_pin = index + 1
        print(f"Selected Roll Pin: {self.roll_pin}")

        # Add code for initializing the roll pin on Arduino here

    def pitch_pin_selected(self, index):
        self.pitch_pin = index + 1
        print(f"Selected Pitch Pin: {self.pitch_pin}")

        # Add code for initializing the pitch pin on Arduino here

# Create the application and run it
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
