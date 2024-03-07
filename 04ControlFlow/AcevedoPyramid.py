def Pyramid():
    stacks = int(input(f'Number of Stacks 1-8: '))
    layer = 0
    if 0 < stacks <= 8:
        for i in range(stacks):
            while 0 < i <= stacks:
                    stacks -= 1
                    layer += 1
                    print(" " * stacks + "#" * layer)
    else:
        print('Thats too many layers!')

Pyramid()

