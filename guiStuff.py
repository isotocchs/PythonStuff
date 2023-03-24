# Put in terminal: pip3 install pysimplegui
import math
import PySimpleGUI as sg

title = "Conversion"
spinList = ["item1", "item2","item3", "item4"]

layout = [
    [sg.Text("Test", font=("Arial",45), key="TextBox1"),sg.Spin(spinList, size=(10,1),font=("Arial",45))],
    [sg.Button("Button Stuff", font=("Arial",45), key="Button1")],
    [sg.Input(font=("Arial",45), size=(20,1))]
    # [sg.Button("Button Stuff", key="Button2")],
    # [sg.Text("Testing Events",font=("Arial",45), enable_events=True, key="TextBox2")]
]


sg.Window(title, layout).read()



# myAppWindow = sg.Window(title, layout)


# while True:
#     event, vaues = myAppWindow.read()

#     if event == sg.WIN_CLOSED:
#         break

    
    # events are triggered by actions
    # any element can trigger and event.
    # The name of the event will be the key (name) of the button or element
    # if event == "Button Stuff":
    #     print("--------------------")
    #     print("I pressed my buttion")
    #     print("--------------------")

    # It is better to use keys than the name in 
    # case you want to name the buttons the same thing
#     if event == "Button1":
#         print("--------------------")
#         print("I pressed my buttion")
#         print("--------------------")
#     if event == "TextBox":
#         print("--------------------")
#         print("I pressed the text box at the bottom")
#         print("--------------------")


# myAppWindow.close()

