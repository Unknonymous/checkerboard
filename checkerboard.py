                           #define the string to repeat
i = 0
row1 = "* * * * "                       #set odd row  
row2 = " * * * *"                       #set even row
for i in range (2, 10):                 #set board loop (a checkerboard is 8 x 8)
    if i % 2 == 1 :                     #check if even or odd row
        print row1                      #print odd row: black white black... 
    else:
        print row2                      #print even row: white black white...
    
#smartmouth comment XD