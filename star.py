""" print the give below pattern, for n number
* * * *
* * * *
* * * *
* * * * """

# take a input from the user 
n = int(input("How much number of pattern you want to print: "))
# outerloop
raw = 1 #for start with the first raw
while (raw<=n): # loop for the n raw
    col = 1
    while (col<=n): #innerloop, for n column
        print("*", end=" ") # printing the * in all column
        col+= 1 #increase the column
    raw += 1 #increase the raw
    print() #add the new line after each line

