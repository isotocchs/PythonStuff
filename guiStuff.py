# Put in terminal: pip3 install pysimplegui
import PySimpleGUI as sg

title = "Conversion"
spinList = ["item1", "item2","item3", "item4"]

layout = [
    [sg.Text("Test", font=("Arial",45), enable_events=True, key="TextBox1", text_color="Blue"),
    sg.Spin(spinList, size=(10,3),font=("Arial",45), key="ItemSpin")],
    [sg.Button("OK", font=("Arial",45), key="Button1")],
    [sg.Input(font=("Arial",45), size=(20,1), background_color="Teal", key="InputBox1")],
    [sg.Button("OK", font=("Arial",45), key="Button2")],
    [sg.Button("Change Element", font=("Arial",45), key="Button3")]

]

# color Options : Black, Blue, Green, Teal, Brown, Yellow, Gray, Purple

# sg.Window(title, layout).read()



myAppWindow = sg.Window(title, layout)


while True:
    event, values = myAppWindow.read()

    # events are triggered by actions
    # any element can trigger and event.
    # The name of the event will be the key (name) of the button or element
    # It is better to use keys than the name in 
    # case you want to name the buttons the same thing

    if event == sg.WIN_CLOSED:
        break




    #Printing Values
    if event == "Button1":
        print("-------------------")
        print("Printing the Values")
        print(values)
        print("-------------------")

    if event == "Button2":
        print("-------------------")
        print("Printing the Values from only the input box")
        print(values["InputBox1"])
        #you can save that info in a variable
        inputBox = values["InputBox1"]
        #we can test that variable to make sure its what we want.
        if inputBox.isnumeric():
            print(inputBox)
        else:
            print("Please put in a number")

        # we can test several cases with a match case clause
        match values["ItemSpin"]:
            case "item1":
                output = "We Selected Item 1"
            case "item2":
                output = "We Selected Item 2"
            case "item3":
                output = "We Selected Item 3"
            case "item4":
                output = "We Selected Item 4"
        print(output)
        print("-------------------")

    #Updating Elements

    if event == "Button3":
        # myAppWindow["TextBox1"].update(values["InputBox1"])
    # You can upadate other things like visibility
        myAppWindow["TextBox1"].update(visible = False)




    
    



myAppWindow.close()

