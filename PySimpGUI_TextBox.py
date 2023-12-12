import PySimpleGUI as sg      

# PySimpleGUI
#has Magna Logo

sg.theme('DarkBlack')
layout = [
    [sg.Text('Enter Roll & Pitch Values')],
    [sg.Text('Roll', size =(15, 1)), sg.InputText()],
    [sg.Text('Pitch', size =(15, 1)), sg.InputText()],
    [sg.Button('Rotate Servos', key='-ROTATE-')],
    [sg.Cancel()]
]   
window = sg.Window('Servo Motor Controller', layout, icon='')   
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)   
finally:      
 while True:
     
    event, values = window.read()   # type: ignore
    
    if event == 'Cancel':
        window.close()
    else:
        if(values[0].isnumeric() and values[1].isnumeric()):#type:ignore
            a = int(float(values[0]))
            b = int(float(values[1]))  
            if(a > 20 or b > 20):
                sg.popup('Enter Values Below 20', icon='')
            else:
                sg.popup('Values Noted Successfully', icon='')
                                       
        else:
            sg.popup('Only Integer Inputs are Accepted', icon='')
