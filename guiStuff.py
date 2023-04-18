# Put in terminal: pip3 install pysimplegui
import PySimpleGUI as sg

title = "Conversion"
spinList = ["in to ft", "ft to in","meter to ft", "ft to meter"]

layout = [
    [sg.Input(font=("Arial",45), size=(20,1), background_color="Green", key="InputBox1"),
    sg.Spin(spinList, size=(10,3),font=("Arial",45), key="ItemSpin"), 
    sg.Button("Convert", font=("Arial",45), key="ConvButt")],
    [sg.Text("Conversion Result", font=("Arial",45), key="TextBox1", text_color="Blue")]
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
    if event == "ConvButt":
        print("-------------------")
        print("Printing the Values")
        something = values["InputBox1"]
        somerith = float(something)
        match values["ItemSpin"]:
            case "in to ft":
                output = "We Selected in to ft"
            case "ft to in":
                output = "We Selected ft to in"
            case "meter to ft":
                output = "We Selected meter to ft"
            case "ft to meter":
                output = "We Selected ft to meter"

        myAppWindow["TextBox1"].update(output)
        # print(values["ItemSpin"])
        # itemSpinInfo = values["ItemSpin"]
        # print(itemSpinInfo)


        # inputBox1Info = values["InputBox1"]
        # print(inputBox1Info)
        # if inputBox1Info.isnumeric():
        #     print(float(inputBox1Info)*5)
        #     myAppWindow["TextBox1"].update(float(inputBox1Info)*5)
        # else:
        #     print("Please put in a number")
        #     myAppWindow["TextBox1"].update(inputBox1Info)


        # inputBox2Info = values["InputBox2"]
        # if inputBox1Info == "Apples":
        #     print("You've selected tjhe best fruit")
        # else:
        #     print("You have the wrong fruit")
        # if inputBox1Info.isnumeric():
        #     print("Thank you for putting in a number")
        # else:
        #     print("Please put in a number")

        # if itemSpinInfo == "ft to in":
        #     print("I have selected ft to in")
        # else: 
        #     print("I have not selected ft to in")
        print("-------------------")
    


    if event == "TextBox1":
        print("-------------------")
        print("I've clicked on the text")
        # print(values)
        print("-------------------")

    if event == "Button4":
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
            case "in to ft":
                output = "We Selected in to ft"
            case "ft to in":
                output = "We Selected ft to in"
            case "meter to ft":
                output = "We Selected meter to ft"
            case "ft to meter":
                output = "We Selected ft to meter"

        myAppWindow["TextBox1"].update(output)

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

