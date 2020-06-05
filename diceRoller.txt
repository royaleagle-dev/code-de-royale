import random
import datetime
import PySimpleGUI as sg


def gen2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    with open ('dicelog.txt', 'a') as file:
        data = str(datetime.datetime.now()) + ":===>  "+str(dice1) + ", "+str(dice2)+"\n"
        file.write(data)
    	
    return (dice1, dice2)

dice = gen2dice

#layout
layout = [
    [sg.Text('A dice rolling Program')],
    [sg.Text(key = '-DICE RESULT-', size = (20, 1))],
    [sg.Button('Generate'), sg.Button('Quit')],
    ]


#create the window
window = sg.Window('Dice Generator',layout)



#Event Loop
while True:
    event, values = window.read()
    if event == 'Generate':
        result = dice()
        print (result)
        window['-DICE RESULT-'].update('You Rolled:     {}'.format(str(result)))
    elif event in (sg.WIN_CLOSED, 'Quit'):
        break
window.close()


