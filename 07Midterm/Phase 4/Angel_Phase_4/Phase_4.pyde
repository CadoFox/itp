unit = 2
grid = 10
canvas = grid * 81
tsl = unit * 4
tpoints = [0,0,tsl,0,0,tsl]

def setup():
    size(canvas, canvas)
    noStroke()

def drawObject(x,y,s):
    push()
    fill(0)
    translate(x,y)
    scale(s)
    triangle(
             tpoints[0],
             tpoints[1],
             tpoints[2],
             tpoints[3],
             tpoints[4],
             tpoints[5],
             )
    triangle(
             tpoints[0],
             tpoints[1] + tsl + unit,
             tpoints[2],
             tpoints[3] + (tsl * 2) + unit,
             tpoints[4],
             tpoints[5] + tsl + unit,
             )
    triangle(
             tpoints[0] + (tsl * 2) + unit,
             tpoints[1] ,
             tpoints[2] + unit ,
             tpoints[3],
             tpoints[4] + (tsl * 2) + unit,
             tpoints[5],
             )
    triangle(
             tpoints[0] + (tsl * 2) + unit,
             tpoints[1] + (tsl * 2) + unit,
             tpoints[2] + unit ,
             tpoints[3] + (tsl * 2) + unit,
             tpoints[4] + (tsl * 2) + unit,
             tpoints[5] + unit,
             )
    rect(
         tpoints[0] + unit,
         tpoints[1] + unit,
         (tsl)*2 - unit,
         (tsl)*2 - unit,
         )
    pop()

def draw():
    global s
    global unit
    x = width
    y = height
    for i in range(1, x, grid):
        for j in range(1, y, grid):
            drawObject(unit * i,unit * j, 1)
