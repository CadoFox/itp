result = 0

def get_power(n):
    base = n
    power = 2
    global result
    result = base ** power
    return result

def print_graph():
    global result
    for i in range(-8, 9):
        get_power(i)
        print('*' * result)

print_graph()

