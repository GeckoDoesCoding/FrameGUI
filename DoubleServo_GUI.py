import PySimpleGUI as sg
import serial
import time

# Replace 'your_serial_port' with the actual serial port your Arduino is connected to
ser = serial.Serial('your_serial_port', 9600)

# Function to send roll and pitch angles to Arduino
def send_angles_to_arduino(roll_angle, pitch_angle):
    # These are simple examples, adjust the pins based on your setup
    roll_servo_pin = 9
    pitch_servo_pin = 10
    
    # Send servo commands to Arduino
    arduino_command = f"{roll_servo_pin},{int(roll_angle)},{pitch_servo_pin},{int(pitch_angle)}\n"
    ser.write(arduino_command.encode())

# Function to draw servo positions on the canvas
def draw_servo_positions(canvas, angle, color):
    canvas.draw_line((100, 50), (100 + int(angle), 50), color=color)

# GUI layout
layout = [
    [sg.Text('Select Roll Angle (0 to 180):'), sg.Slider(range=(0, 180), orientation='h', size=(20, 15), default_value=90, key='-ROLL-')],
    [sg.Text('Select Pitch Angle (0 to 180):'), sg.Slider(range=(0, 180), orientation='h', size=(20, 15), default_value=90, key='-PITCH-')],
    [sg.Button('Set Angles', key='-SET-')],
    [sg.Button('About'), sg.Button('QUIT')],
    [sg.Canvas(size=(200, 100), background_color='white', key='-ROLL-CANVAS-')],
    [sg.Canvas(size=(200, 100), background_color='white', key='-PITCH-CANVAS-')],
]

# Create the window
window = sg.Window('Servo Motor Control', layout)

# Get the canvas elements
roll_canvas_elem = window['-ROLL-CANVAS-']
pitch_canvas_elem = window['-PITCH-CANVAS-']

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'QUIT':
        break

    elif event == 'About':
        sg.popup('Logic Don\'t Care Software\nServo Motor Ver 1.0\nAugust 2022', title='About')

    elif event == '-SET-':
        roll_angle = values['-ROLL-']
        pitch_angle = values['-PITCH-']

        # Send angles to Arduino
        send_angles_to_arduino(roll_angle, pitch_angle)

        # Draw servo positions on the canvases
        draw_servo_positions(roll_canvas_elem, roll_angle, 'red')
        draw_servo_positions(pitch_canvas_elem, pitch_angle, 'blue')

        # Add a small delay for better visualization
        time.sleep(0.1)

# Close the window
window.close()
