# Phase 4

## Updated Variables + Setup

        unit = 10
        grid = 10
        canvas = grid * 81
        tsl = unit * 4
        tpoints = [0,0,tsl,0,0,tsl]

        def setup():
            size(canvas, canvas)
            noStroke()



### Once I moved on to the next phase, I realized that my initial system for making the code "dynamic" gets in the way of the scaling requiements for phase 4. As a result, I separated the variable that determined the size from the units used to construct the shape. This allows me to use the unit as a division of the grid, which gives me the ability to scale the shape while the size of the canvas stays the same

## Updated shape drawing

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

## This part is almost the exact same as the previous phase, except for the method I used to draw the rectangle, which just avoids having things as hard coded values and references the unit size a bit better to make it more responsive

# Updated Draw Function

        def draw():
            global s
            global unit
            x = width
            y = height
            for i in range(1, x, grid):
                for j in range(1, y, grid):
                    drawObject(unit * i,unit * j, 1)

## I used the nested for loops, using the grid value and NOT the unit value to determine by what the counter needs to count by to place the shapes. I then just referenced the two counters in the drawObject function in reference to the unit and NOT the grid, so that the spacing between them wouldnt change, since its referencing the division used to draw the shape, not the division to make the grid

# Challenges / Closing thoughts
## I was a bit clouded by my own excitement to make this project my own I feel. I did like challenging myself with making the initial code "responsive" while still hitting all the requirements, however when it came time to meet the 4th phase requirements, it was clear this would need its own documentation, as I would have to significaantly change the structure in order to be able to use the nested for loops properly. Lesson learned once again





