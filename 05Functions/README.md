# Code
## This program prints the equation 'y = x^2', represented by 'result = x^n'


    def get_power(x,n):
        result = 0 
        result = x ** n
        return result

    def print_graph():
        for i in range(-8, 9):
        print('*' * get_power(i,2))

    print_graph()

# How it Works

## Getting Power value

    def get_power(x,n):
        result = 0 
        result = x ** n
        return result

### Here the function takes in a base and an exponent, labled "x" and "n". Then, a result variable is initialized, and then assigned with the result of "x" to the power of "n". The function will return the resulting value 

## Printing the Graph

    def print_graph():
        for i in range(-8, 9):
            print('*' * get_power(i,2))

    print_graph()

### Here, a "for" loop is used for creating the series of lines representing the equation. The index of the for loop is passed on to the get_power function, and the result is used inside a print function to concatenate the "*" character in each line according to the value stored in "result" after "i" goes through the get_power function

# Bonus: 
## less efficient version that does also work!

    result = 0
    
    def get_power(n):
        base = n
        power = 2
        global result
        result = base ** power
    
    def print_graph():
        global result
        for i in range(-8, 9):
            get_power(i)
            print('*' * result)

    print_graph()

### The improvement from here was mainly reducing the number of variables stored. I initially used a global result value as the storage place for the line being printed at a given moment, and then I remembered the value can be passed on using "return" instead, which allowed me to drastically strip down the code.

### ~also I realized that this version would not meet the requirements for what both functions are supposed to be taking in~
