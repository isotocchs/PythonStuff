import PySimpleGUI as sg
from time import time
from random import randint

title = "Snake"

graphSize = 400
numberOfBlocks = 10
blockSize = graphSize/numberOfBlocks


def placeRandomFruit():
    fruitPosition = randint(0,numberOfBlocks-1),randint(0,numberOfBlocks-1)
    while fruitPosition in snakePosition:
        fruitPosition = randint(0,numberOfBlocks-1),randint(0,numberOfBlocks-1)
    return fruitPosition

def positionToPixel(cell):
    topLeft = cell[0]*blockSize,cell[1]*blockSize
    bottomRight = topLeft[0]+blockSize,topLeft[1]+blockSize
    return topLeft, bottomRight

snakePosition = [(4,4),(3,4),(2,4)]

#fruitPlacement
fruitPosition = placeRandomFruit()
fruitEaten = False

possibleDirections = {"left":(-1,0),"right":(1,0),"down":(0,-1),"up":(0,1)}
direction = possibleDirections["up"]

playArea = sg.Graph(
        canvas_size=(graphSize,graphSize),
        graph_bottom_left=(0,0),
        graph_top_right=(graphSize,graphSize),
        background_color="#000000"
        )

layout = [[playArea]]


myAppWindow = sg.Window(title, layout, return_keyboard_events=True)

startTime = time()

while True:
    event, values = myAppWindow.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    if event == "Left:2063660802":
        direction = possibleDirections["left"]
    if event == "Right:2080438019":
        direction = possibleDirections["right"]
    if event == "Up:2113992448":
        direction = possibleDirections["up"]
    if event == "Down:2097215233":
        direction = possibleDirections["down"]


    timeSinceStartOfGame = time()-startTime
    if timeSinceStartOfGame >= 0.5:
        startTime = time()

        # # snake update - snakePosition = [(4,4),(3,4),(2,4)]
        newSnakeHead = (snakePosition[0][0]+direction[0],snakePosition[0][1]+direction[1])
        snakePosition.insert(0,newSnakeHead)
        snakePosition.pop() #remove last part of snake
        
        # snake ate the fruit
        if snakePosition[0] == fruitPosition:
            fruitPosition = placeRandomFruit()
            fruitEaten = True

        # #clear the graph
        playArea.DrawRectangle((0,0),(graphSize,graphSize),"#000000")

        #draw fruit
        topLeft,bottomRight  = positionToPixel(fruitPosition)
        playArea.DrawRectangle(topLeft,bottomRight,"red")

        #draw snake - snakePosition = [(4,4),(3,4),(2,4)]
        for index, part in enumerate(snakePosition):
            topLeftS,bottomRightS  = positionToPixel(part)
            if index == 0:
                color = "orange"
            else:
                color = "green"
            playArea.DrawRectangle(topLeftS,bottomRightS,color)


myAppWindow.close()