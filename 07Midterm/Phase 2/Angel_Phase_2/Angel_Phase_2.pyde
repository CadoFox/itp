triangleSL = 20
trianglepoint1 = [0,0]
trianglepoint2 = [triangleSL,0]
trianglepoint3 = [0,0]

def setup():
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) # Fill in with black color
    triangle (0, 0, 20, 0, 0, 20)
    pop()

def draw():
    drawObject(0,0,1)
    drawObject(0,200,1)
