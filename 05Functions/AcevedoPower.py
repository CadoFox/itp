def get_power(x,n):
    result = 0 
    result = x ** n
    return result

def print_graph():
    for i in range(-8, 9):
        print('*' * get_power(i,2))

print_graph()

##
