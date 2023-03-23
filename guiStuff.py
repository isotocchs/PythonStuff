# Put in terminal: pip3 install pysimplegui

import PySimpleGUI as sg

title = "Conversion"
spinList = ["item1", "item2","item3", "item4"]

layout = [
    [sg.Text("Test"),sg.Spin(spinList)],
    [sg.Button("Button Stuff")],
    [sg.Input()]
]
sg.Window(title, layout).read()



# myAppWindow = sg.Window(title, layout)

# while True:
#     event, vaues = myAppWindow.read()

#     if event == sg.WIN_CLOSED:
#         break

#     # events are triggered by actions
#     # any element can trigger and event.
#     # The name of the event will be the key (name) of the button or element
#     # if event == "Button Stuff":
#     #     print("--------------------")
#     #     print("I pressed my buttion")
#     #     print("--------------------")


# myAppWindow.close()

