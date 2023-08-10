import PySimpleGUI as sg
from pathlib import Path


sg.set_options(font=("Arial",35))
title = "Text Editor"

smiley = ["Happy",[":)",":D","xD"], "Sad",[":(","T_T"],"other",[":3"]]

menuLayout = ["File",["Open","---","Save","Something","---","Exit"]]
menuLayout2 = ["Tools",["Word Count", "Char Count"]]
menuLayout3 = ["Add",smiley]

layout = [
        [sg.ButtonMenu("File",menuLayout, key="FileMenu", button_color="#000000"),
        sg.ButtonMenu("Tools",menuLayout2, key="ToolsMenu", button_color="#000000"),
        sg.ButtonMenu("Smiley",menuLayout3, key="SmileMenu", button_color="#000000")],
        [sg.Text("Untitled", key="documentName")],
        [sg.Multiline("",expand_y=True, size=(20,10), key="Multi")]
        ]

myAppWindow = sg.Window(title, layout)

while True:
    event, values = myAppWindow.read()
    

    if event == "FileMenu":
        match values["FileMenu"]:
            case "Open":
                filePath = sg.popup_get_file("Open", no_window=True)
                if filePath:
                    file = Path(filePath)
                    myAppWindow["Multi"].update(file.read_text())
                    myAppWindow["documentName"].update(filePath.split("/")[-1])
            case "Save":
                filePath = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
                file = Path(filePath)
                file.write_text(values["Multi"])
                myAppWindow["documentName"].update(filePath.split("/")[-1])

            case "Something":
                myAppWindow["Multi"].update("Somthing")
            case "Exit":
                myAppWindow["Multi"].update("Exit")
    
    if event == "ToolsMenu":
        match values["ToolsMenu"]:
            case "Word Count":
                allText = values["Multi"]
                print(allText)
                wordCount = allText.replace("\n"," ").split(" ").__len__()
                #make a pop up
                sg.popup(f"Number of words: {wordCount}", keep_on_top=True)

    if event == "SmileMenu":
        match values["SmileMenu"]:
            case ":)":
                currentText = values["Multi"]
                newText = currentText + " "+ values["SmileMenu"]
                myAppWindow["Multi"].update(newText)
            case ":(":
                currentText = values["Multi"]
                newText = currentText + " "+ values["SmileMenu"]
                myAppWindow["Multi"].update(newText)
            case ":3":
                currentText = values["Multi"]
                newText = currentText + " "+ values["SmileMenu"]
                myAppWindow["Multi"].update(newText)
    

    if event == sg.WIN_CLOSED:
        break

myAppWindow.close()

