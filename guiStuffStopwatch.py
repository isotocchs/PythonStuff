import PySimpleGUI as sg
from time import time

def create_window():

  sg.set_options(font=("Arial",45))
  title = "Stopwatch"

  layout = [
          # [sg.Push(),sg.Image("cross2copy.png",pad=0,enable_events=True, key="Closer")],
          [sg.VPush()],
          [sg.Text("Time", key="TextDisplay")],
          [sg.Button("Start", button_color=("#ee1811","#090602"), key="StartStop" ),
          sg.Button("Lap", button_color=("#2312ED","#DCED12"), key="LapButton")],
          [sg.Column([[]], key="Laps")],
          [sg.VPush()]
            ]

  return sg.Window(title, layout, size = (300,300), element_justification="center")
#you can set specific window Size and justification
myAppWindow = create_window()

startTime = 0
active = False
laps = 1

while True:
    event, values = myAppWindow.read(timeout=10)

    if event in (sg.WIN_CLOSED, "Closer"):
        break

    if event == "StartStop":
      if active:
        active = False
        myAppWindow["StartStop"].update("Reset")
      else:
        startTime = time()
        active = True
        myAppWindow["StartStop"].update("Stop")

    if active:
      elapsedTime = round(time() - startTime,1)
      myAppWindow["TextDisplay"].update(elapsedTime)

    if event == "LapButton":
      myAppWindow.extend_layout(myAppWindow["Laps"], [[sg.Text(laps, font=("Arial",25)),
                                sg.VSeparator(),sg.Text(elapsedTime, font=("Arial",25))]])
      laps += 1
myAppWindow.close()

