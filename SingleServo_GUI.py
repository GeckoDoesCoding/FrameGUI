import PySimpleGUI as sg
import serial  
ser = serial.Serial('COM4', 9600)

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)   

# Function to send the servo angle to Arduino
def send_angle_to_arduino(angle):
    servo_pin = 9
    
    # Send servo command to Arduino
    arduino_command = f"{servo_pin},{int(angle)}\n"
    ser.write(arduino_command.encode())
    
# GUI layout
sg.theme('Dark Black')
layout = [
    [sg.Text('Select Angle:')],
    [sg.Slider(range=(0, 180), orientation='h', size=(20, 15), default_value=0, key='-ANGLE-')],
    [sg.Button('Set Angle', key='-SET-')],
    [sg.Button('About'), sg.Button('QUIT')],
]

# Create the window
window = sg.Window('SimpleGUI', layout, icon='c:/Users/shoukulk/Desktop/Work/Logos/MagnaLogo.ico', size= (300,150))

# Event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'QUIT':
        serial.Serial("COM4", 9600).close()
        break

    elif event == 'About':
        sg.popup('Running only for a Single Servo Setup', title='About')

    elif event == '-SET-':
        angle = values['-ANGLE-']
        send_angle_to_arduino(angle)

# Close the window
serial.Serial("com4", 9600).close()
window.close()
