import tkinter as tk
from tkinter import Scale, Button, Label
import serial

# Replace 'COM3' with the actual serial port your Arduino is connected to
ser = serial.Serial('COM3', 9600)

def set_angles():
    roll_angle = roll_slider.get()
    pitch_angle = pitch_slider.get()
    
    # Format the data as per your Arduino code expectations
    data = f"Roll:{roll_angle}\nPitch:{pitch_angle}\n"
    
    # Send data to Arduino
    ser.write(data.encode())
    
    print(f"Setting Roll: {roll_angle}, Pitch: {pitch_angle} to Arduino")

# Create the main window
root = tk.Tk()
root.title("Roll Pitch Control")

# Pitch Control
pitch_label = Label(root, text="Pitch Control")
pitch_label.grid(row=0, column=0, padx=10, pady=5)
pitch_slider = Scale(root, from_=0, to=20, orient="horizontal", length=200)
pitch_slider.grid(row=0, column=1, padx=10, pady=5)

# Roll Control
roll_label = Label(root, text="Roll Control")
roll_label.grid(row=1, column=0, padx=10, pady=5)
roll_slider = Scale(root, from_=0, to=20, orient="horizontal", length=200)
roll_slider.grid(row=1, column=1, padx=10, pady=5)

# Set Angles Button
set_angles_button = Button(root, text="Set Angles", command=set_angles)
set_angles_button.grid(row=2, column=0, columnspan=2, pady=10)

# Quit Button
quit_button = Button(root, text="QUIT", command=root.destroy)
quit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
