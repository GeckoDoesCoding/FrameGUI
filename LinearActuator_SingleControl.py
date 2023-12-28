import PySimpleGUI as sg
import serial
ser = serial.Serial('COM5', 9600)
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
# Function to send the pitch values to Arduino
def send_pitch_to_arduino(pitch):
    servo_pin = 10
    # Send pitch command to Arduino
    arduino_command = f"{servo_pin},{pitch}\n"
    ser.write(arduino_command.encode())
# GUI layout
sg.theme('DarkBlack')
layout = [
    [sg.Text('Enter Pitch Value')],
    [sg.Text('Roll', size=(15, 1)), sg.InputText()],
    [sg.Text('Pitch', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('SimpleGUI', layout, icon='c:/Users/shoukulk/Desktop/Work/Logos/MagnaLogo.ico', size=(300, 150))
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    while True:
        event, values = window.read()  # type: ignore
        if event == 'Cancel':
            window.close()
        else:
            if values[0].isnumeric() and values[1].isnumeric(): #type:ignore
                # Extract pitch value
                pitch = int(float(values[1]))

                if pitch > 20:
                    sg.popup('Enter Pitch Value Below 20', icon='c:/Users/shoukulk/Desktop/Work/Logos/MagnaLogo.ico')
                else:
                    # Send pitch value to Arduino
                    send_pitch_to_arduino(pitch)

                    sg.popup('Pitch Value Noted Successfully', icon='c:/Users/shoukulk/Desktop/Work/Logos/MagnaLogo.ico')
            else:
                sg.popup('Error', 'Only Numeric Inputs are Accepted',)

