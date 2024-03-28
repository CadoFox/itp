unit = 50
tsl =  unit * 4
tpoints = [0,0,tsl,0,0,tsl]

def setup():
    size(tsl * 2 + unit * 3, tsl * 2 + unit * 3)
    noStroke()

def drawObject(x,y,s):
    push()
    global unit
    global tsl
    global tpoints
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
         unit * 7,
         unit * 7,
         )
    pop()

def draw():
    drawObject(unit,unit,1)
