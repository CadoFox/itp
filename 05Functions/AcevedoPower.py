def get_power(x,n):
    result = 0 
    result = x ** n
    return result

def print_graph(n):
    for i in range(-8, 9):
        print('*' * get_power(i,n))

print_graph(2)
