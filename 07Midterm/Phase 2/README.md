# Phase 2

## Parameters
### My goal was to have the program generate the shapes as dynamically as possible. As such, I had to figure out how to use as little initial parameters as possible instead of just hard coding all the values I needed. 

        unit = 50
        tsl =  unit * 4
        tpoints = [0,0,tsl,0,0,tsl]

### I settled with defining a unit size, and using that value to do all the math involved with determining the length of the sides of the triangles. I also used a variable asigned to a single variable, so that I could reference the variable that determines the side length, allowing everything to adjust automatically any time the unit size is changed.

## Setup
        def setup():
            size(tsl * 2 + unit * 3, tsl * 2 + unit * 3)
            noStroke()
### In this setup function, I aimed to also make the size of the canvas dynamic as well. To do this, I did some basic math using the side length and unit size. This would allow for the canvas size to change dynamically if *either the unit size or the side length of the triangle* were to be changed


## drawObject
### In my goal of making this code as dynamic as possible, I also wanted it to be fairly readable.
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

 ### The initial triangle is built by referencing the individual values of the "tpoints" list.

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
### I then devised this method for creating the rest of them, which does all the adjustments of the position of each point based off of the initial triangle made by the "tpoints" list, referencing the side length "tsl" and the unit size "unit" to do the math involved with moving them around. This again allows for the unit size to be changed, and the shapes automatically adjust. I also took advantage of the triangle being drawn agnostic of the order of points, meaning I simply needed to move one of the points to the correct relative location and the triangle would be effectively "rotated"

            rect(
                tpoints[0] + unit,
                tpoints[1] + unit,
                unit * 7,
                unit * 7,
                )
            pop()

### I then created the middle rectangle, employing the same method using the unit size to set the parameters. I also just referenced the first point of the initial triangle for the upper left of the rectangle, so that its position is relative to wherever that is.
 
## Draw

        def draw():
            drawObject(unit,unit,1)

### Finally, I call the drawObject funtion, and use the unit size to place the drawing

# ChatGPT Disclosure

### I did use ChatGPT for one specific problem. 
### My initial plan was to use individual variables for each point of the triangle for the "triangle()" object, as such

        tpoint1 = [0,0]
        tpoint2 = [tsl,0]
        tpoint3 = [0,tsl]

### I tried a few things myself, and had a hard time figuring out how to *search* for the problem online, and could not find anything on the specific result I was after. So I first asked if the ChatGPT model was familiar with processing, which is confirmed, and then presented my problem with the following prompt:

        how can I use a list of integers, assigned to a variable, in a way that allows me to use that list to convert it into just a series of comma separated values that I can then use for the triangle() function.

        for example, heres what I have in my global variables

        tpoint1 = [0,0]
        tpoint2 = [40,0]
        tpoint3 = [0, 40]

        and I want to be able to use those variables as the points of the triangle in the triangle() function. How could I do that?

### It then instructed me to use asterisks before each reference to the points to unpack the values (note: in hindsight, using the word "unpack" would likely have been useful in my search...), as follows
#### *note: I hadnt seen this before, so I also asked if the asterisk was what was unpacking the values, which it confirmed*

        triangle(*tpoint1, *tpoint2, *tpoint3)

### but I then discovered that processing does not use the same syntax for that. I passed on the error message to the model with the following prompt:

        I recieved this error when I tried that

        mismatched input '*' expecting DOUBLESTAR

### and *this* is when it instructed me to just reference the individual values of the list with the brackets. Lesson learned!
