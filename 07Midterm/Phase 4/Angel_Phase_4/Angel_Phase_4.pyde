unit = 10
s = .5
tsl =  (unit/s) * 4
tpoints = [0,0,tsl,0,0,tsl]

def setup():
    size(520, 520)
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
         (tsl) + (unit/s) * 3,
         (tsl) + (unit/s) * 3,
         )
    pop()

def draw():
    global s
    global unit
    x = width
    y = height
    for i in range(1, x, unit):
        for j in range(1, y, unit):
            drawObject(unit * i,unit * j, s)
