import PySimpleGUI as sg

#A simple Python GUI Application
def calculate(expression):
    result = eval(str(expression))
    return (result)
   
print(calculate(2+5+ (100/2)))

#layout
layout = [
        [sg.Text('A mini Python Calculator')],
        [sg.Input(size = (50, 1))],
        
        ]

#window
window = sg.Window('Mini Calculator', layout = layout)

#event loop
while True:
   event, values = window.read()



