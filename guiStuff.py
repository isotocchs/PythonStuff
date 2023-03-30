# Put in terminal: pip3 install pysimplegui
import PySimpleGUI as sg

title = "Conversion"
spinList = ["in to ft", "ft to in","meter to ft", "ft to meter"]

layout = [
    [sg.Input(font=("Arial",45), size=(20,1), background_color="Green", key="InputBox1"),
    sg.Spin(spinList, size=(10,3),font=("Arial",45), key="ItemSpin"), 
    sg.Button("Convert", font=("Arial",45), key="Button1")],
    [sg.Text("Test", font=("Arial",45), enable_events=True, key="TextBox1", text_color="Blue")]
    # [sg.Input(font=("Arial",45), size=(20,1), background_color="Teal", key="InputBox2")],
    # [sg.Button("OK", font=("Arial",45), key="Button3")],
    # [sg.Button("Change Element", font=("Arial",45), key="Button4")]

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
        itemSpinInfo = values["ItemSpin"]
        inputBox1Info = values["InputBox1"]
        inputBox2Info = values["InputBox2"]
        if inputBox1Info.isnumeric():
            print("Thank you for putting in a number")
        else:
            print("Please put in a number")

        if itemSpinInfo == "item3":
            print("I have selected Item 3")
        else: 
            print("I have not selected Item 3")
        print("-------------------")
    
    if event == "TextBox1":
        print("-------------------")
        print("I've clicked on the text")
        # print(values)
        print("-------------------")

    if event == "Button2":
        print("-------------------")
        print("Printing the Values from only the input box")
        # print(values["InputBox1"])
        #you can save that info in a variable
        # inputBox = values["InputBox1"]
        #we can test that variable to make sure its what we want.
        # if inputBox.isnumeric():
        #     print(inputBox)
        # else:
        #     print("Please put in a number")

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
#     x = 45-3
#     if event == "Button4":
#         # myAppWindow["TextBox1"].update(x)
# # You can upadate other things like visibility
#         myAppWindow["TextBox1"].update(visible = False)
    
#     if event == "Button3":
#         # myAppWindow["TextBox1"].update(x)
# # You can upadate other things like visibility
#         myAppWindow["TextBox1"].update(visible = True)




    
    



myAppWindow.close()

