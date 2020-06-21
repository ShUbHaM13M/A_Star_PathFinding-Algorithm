
import pygame
import sys
import math
import os
from tkinter import messagebox
from tkinter import *

screenWidth = 500
screenHeight = 500

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("A*")
clock = pygame.time.Clock()

class Node(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.parent = None
        self.isObs = False
        self.isClosed = False
        self.value = 1
    
    
    def addNeighbours(self, grid):
        i = self.x 
        j = self.y

        if x < cols - 1 and grid[self.x + 1][j].isObs == False:
            self.neighbors.append(grid[self.x + 1][j])

        if x > 0 and grid[self.x - 1][j].isObs == False:
            self.neighbors.append(grid[self.x - 1][j])

        if y < rows - 1 and grid[self.x][y + 1].isObs == False:
            self.neighbors.append(grid[self.x][j + 1])

        if y > 0 and grid[self.x][y - 1].isObs == False:
            self.neighbors.append(grid[self.x][j - 1])

cols = 25
grid = [0 for i in range(cols)]
rows = 25
openSet = []
closedSet = []

nodeWidth = screenWidth / cols
nodeHeight = screenHeight / rows
nodeMargin = 4

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 200)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
TEAL = (0, 153, 153)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)

cameFrom = []

for i in range(cols):
    grid[i] = [0 for i in range(rows)]

for i in range(cols):
    for j in range(rows):
        grid[i][j] =  Node()
        grid[i][j].x = i
        grid[i][j].y = j

startNode = grid[2][5]
endNode = grid[15][15]

pygame.init()
openSet.append(startNode)   

isRunning = True

def draw():
    
    for x in range(cols):
        for y in range(rows):
            
            color = WHITE

            temp = grid[x][y]
            
            if not temp.isObs:
                color = WHITE
            else:
                color = BLACK
            if temp == startNode:
                color = RED
            elif temp == endNode:
                color = GREEN
            
            pygame.draw.rect(screen, color, (temp.x * nodeWidth, temp.y * nodeHeight, nodeWidth - nodeMargin, nodeHeight - nodeMargin))
    
    pygame.display.flip()
    pygame.display.update()

def onContinueBtnClick():
    window.destroy()

window = Tk("A* pathFinding AI")
window.title("A* pathFinding AI")
# window.wm_title = ("A* pathfinding AI")

Label(window, text = "Left click to draw walls").grid(row=1, pady=3)
Label(window, text = "Right click to remove walls").grid(row=2, pady=3)
Label(window, text = "L_Shift + LeftMouse click to change the start position").grid(row=3, pady=3)
Label(window, text = "L_Ctrl + LeftMouse click to change the end position").grid(row=4, pady=3)
Label(window, text = "After placing the nodes press Space to continue")

Button(window, text = "Continue ?", command = onContinueBtnClick).grid(row=6, pady=2)

window.update
window.mainloop()

while isRunning:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                selectedNodeX = pos[0]
                selectedNodeY = pos[1]
                x = selectedNodeX // (screenWidth // cols)
                y = selectedNodeY // (screenHeight // rows)
    
                grid[x][y] = grid[x][y]

                if grid[x][y] != startNode and grid[x][y] != endNode:
                    if grid[x][y].isObs == False:
                        grid[x][y].isObs = True

            except AttributeError:
                pass
        
        elif pygame.mouse.get_pressed()[2]:
            try:
                pos = pygame.mouse.get_pos()
                selectedNodeX = pos[0]
                selectedNodeY = pos[1]
                x = selectedNodeX // (screenWidth // cols)
                y = selectedNodeY // (screenHeight // rows)
                if grid[x][y] != startNode and grid[x][y] != endNode:
                    if grid[x][y].isObs == True:
                        grid[x][y].isObs = False

            except AttributeError:
                pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                isRunning = False

            elif event.key == pygame.K_LSHIFT:
                pos = pygame.mouse.get_pos()
                x = pos[0] // (screenWidth // cols)
                y = pos[1] // (screenHeight // rows)
                startNode = grid[x][y]
                openSet.clear()
                openSet.append(startNode)

            elif event.key == pygame.K_LCTRL:
                pos = pygame.mouse.get_pos()
                x = pos[0] // (screenWidth // cols)
                y = pos[1] // (screenHeight // rows)
                endNode = grid[x][y]
        
        clock.tick(60)
        draw()
            
        
for x in range(cols):
    for y in range(rows):
        grid[x][y].addNeighbours(grid)
    
def heuristic(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def main():

    if len(openSet) > 0:
        lowestIndex = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[lowestIndex].f:
                lowestIndex = i

        current = openSet[lowestIndex]
        if current == endNode:
            print(current.f)
            pygame.draw.rect(screen, RED, (startNode.x * nodeWidth, startNode.y * nodeHeight, nodeWidth - nodeMargin, nodeHeight - nodeMargin), 1 )
            pygame.display.update()
            temp = current.f
            for i in range(round(current.f)):
                current.isClosed = False
                pygame.draw.rect(screen, BLUE, (current.x * nodeWidth, current.y * nodeHeight, nodeWidth - nodeMargin, nodeHeight - nodeMargin))
                pygame.display.update()
                current = current.parent
            pygame.draw.rect(screen, GREEN, (endNode.x * nodeWidth, endNode.y * nodeHeight, nodeWidth - nodeMargin, nodeHeight - nodeMargin))
            pygame.display.update()

            
            Run = True
            while Run:
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                        ag = False
                        break
            pygame.quit()
        

    openSet.pop(lowestIndex)
    closedSet.append(current)

    neighbors = current.neighbors
    for i in range(len(neighbors)):
        neighbor = neighbors[i]
        if neighbor not in closedSet:
            G = current.g + current.value
            if neighbor in openSet:
                if neighbor.g > G:
                    neighbor.g = G 
            else:
                neighbor.g = G
                openSet.append(neighbor)

        neighbor.h = heuristic(neighbor, endNode)
        neighbor.f = neighbor.g + neighbor.h

        if neighbor.parent == None:
            neighbor.parent = current

    for i in range(len(openSet)):
        temp = openSet[i]
        pygame.draw.rect(screen, TEAL, (temp.x * nodeWidth, temp.y * nodeHeight, nodeWidth - nodeMargin, nodeHeight - nodeMargin))
        pygame.display.update()

    for i in range(len(closedSet)):
        if closedSet[i] != startNode:
            temp = closedSet[i]
            pygame.draw.rect(screen, CYAN, (temp.x * nodeWidth, temp.y * nodeHeight, nodeWidth - nodeMargin, nodeHeight - nodeMargin))
            pygame.display.update()

    current.isClosed = True

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()