import PySimpleGUI as sg


title = "Calculator"
layout = [[sg.Text("Output", font=("Arial",45))],
          [sg.Button("Clear", font=("Arial",45)),sg.Button("Enter", font=("Arial",45))],
          [sg.Button(7, font=("Arial",45)),sg.Button(8, font=("Arial",45)),sg.Button(9, font=("Arial",45)),sg.Button("*", font=("Arial",45))],
          [sg.Button(4, font=("Arial",45)),sg.Button(5, font=("Arial",45)),sg.Button(6, font=("Arial",45)),sg.Button("/", font=("Arial",45))],
          [sg.Button(1, font=("Arial",45)),sg.Button(2, font=("Arial",45)),sg.Button(3, font=("Arial",45)),sg.Button("-", font=("Arial",45))],
          [sg.Button(0, font=("Arial",45)),sg.Button(".", font=("Arial",45)),sg.Button("+", font=("Arial",45))]]


myAppWindow = sg.Window(title, layout)

while True:
    event, values = myAppWindow.read()

    if event == sg.WIN_CLOSED:
        break



myAppWindow.close()

