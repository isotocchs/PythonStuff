import PySimpleGUI as sg
from random import randint

title = "Random Teams"
sg.set_options(font=("Arial",45))

layout = [[sg.Button("Random", button_color=("#ee1811","#090602"), key="RandomButton")],
[sg.Multiline("",expand_y=True, size=(30,20), key="Multi")]]

myAppWindow = sg.Window(title, layout, resizable=True)

classNamesP1 = [
  "Aenlle, Dante",
  "Bonilla, Sebastian",
  "Bradley, Rocco",
  "Cros, Adrian",
  "Diaz, Lucas",
  "Duran Iglesias, Lucas",
  "Garces, Andres",
  "Gasca, Matthew",
  "Gomez-Rivera, Leonardo",
  "Marzo, Anthony",
  "Nazario, Lucas",
  "Pouza, Ethan",
  "Rendon, Luis",
  "Rodriguez del Rey, Randy",
  "Rodriguez del Rey, Rick",
  "Rodriguez, Javier",
  "Ros, Matthew",
  "Vazquez , Andres",
]

classNamesP7 = [
  "Anthony Alfonso",
  "Alfredo Arreaza",
  "Gabriel Barquero",
  "John Brown",
  "Marco Cortes",
  "Lucas D Diaz",
  "Gabriel Robert Garcia",
  "Darriel Harper",
  "Jayzer Mansour",
  "Dante Vegliante",
]

while True:
    event, values = myAppWindow.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "RandomButton":
        index = 1
        groupNum = 1
        newText = ""
        myAppWindow["Multi"].update(newText)
        while(len(classNamesP7)>0):
            selection = randint(0,len(classNamesP7)-1)
            randomName = classNamesP7.pop(selection)
            newText = newText + "\n Group: "+str(groupNum)+" "+ randomName
            if index%3 == 0:
                groupNum+=1
            index+=1

        myAppWindow["Multi"].update(newText)

myAppWindow.close()