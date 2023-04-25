import PySimpleGUI as sg


def create_window(themeInput):
    sg.theme(themeInput)
    sg.set_options(font=("Arial",45), border_width=12)

    #all options available (https://www.pysimplegui.org/en/latest/call%20reference/#application-wide-configuration-settings-set_options-etc)
    button_size = (2,1) #size not in pixels but in characters

    title = "Calculator" # right_click_menu=theme_menu
    layout = [[sg.Text("",
                        expand_x= True, 
                        justification="right", 
                        pad=(10,20),
                        right_click_menu=theme_menu,
                        key="TextOutput")],
            [sg.Button("Clear", expand_x=True),sg.Button("Enter", expand_x=True)],
            [sg.Button(7, size=(2,1)),sg.Button(8, size=(2,1)),sg.Button(9, size=(2,1)),sg.Button("*", size=(2,1))],
            [sg.Button(4, size = button_size),sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button("/", size = button_size)],
            [sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button("-", size = button_size)],
            [sg.Button(0, expand_x= True),sg.Button(".", size = button_size),sg.Button("+", size = button_size)]]

    return sg.Window(title, layout)


theme_menu = ["menuName",["Python", "random", "LightGrey1", "Black"]]
# myAppWindow = sg.Window(title, layout)

myAppWindow = create_window("Python")

currentNumber = []
allOperations = []


while True:
    event, values = myAppWindow.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        myAppWindow.close()
        myAppWindow = create_window(event)
    
    if event in ["0","1","2","3","4","5","6","7","8","9","."]:
        currentNumber.append(event)
        numString = "".join(currentNumber)
        myAppWindow["TextOutput"].update(numString)

    if event in ["+","-","/","*"]:
        allOperations.append("".join(currentNumber))
        currentNumber = []
        allOperations.append(event)
        print(allOperations)
        myAppWindow["TextOutput"].update("")

    if event == "Enter":
        allOperations.append("".join(currentNumber))
        print(allOperations)
        print("".join(allOperations))
        result = eval("".join(allOperations))
        print(result)
        myAppWindow["TextOutput"].update(result)
        allOperations = []

    if event == "Clear":
        currentNumber = []
        allOperations = []
        myAppWindow["TextOutput"].update("")




myAppWindow.close()

