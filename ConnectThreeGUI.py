import PySimpleGUI as sg 

MAX_ROWS = MAX_COL = 3

layout = [[sg.Button(' ', size=(10,5), key=(i,j), pad=(10,10)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

window = sg.Window('Tic Tac Toe', layout)

while True:
    sg.popup("It's your turn.")
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    window[event].update('X', button_color=('black', 'white'))


window.close()
