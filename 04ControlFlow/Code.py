count = 0
countby = 10
listofnumbers = range(0, 100, countby)    

for index in listofnumbers:
     if index % 5 == 0 and index % 8 == 0:
        print(index)
         


