firstName = input('First Name:')
middleInit = input('Middle Initial:')
lastName = input('Last Name:')
name = (f'{firstName}{middleInit}{lastName}')
fname = (f'{firstName} {middleInit}. {lastName}')

def PrintStuff():
    print(f'{fname}', '- Number of Letters:', len(name))
    print(f'hello, {fname}')

PrintStuff()

