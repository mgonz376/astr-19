'''This program will use numpy to define the type of data that 
results from each function'''

import numpy as np 

def main():
    x = 3.0
    y = 5.0
    a = 2
    b = 6
    c = 4.0
    d = 1

#This program will print the sum of two floating point numbers

x = 3.0

y = 5.0

print(x+y)

#This function will print out the data type of the resulting sum

print(type(x+y))

#This function will print the difference between two integers

a = 2

b = 6

print(a - b)

#This function will print out the data type of the resulting difference

print(type(a-b))

#This program will print the product of a floating point number 
#and an integer

c = 4.0

d = 1

print(c*d)

#This function will print out the data type of the resulting product

print(type(c*d))

#This will execute the main function

if __name__ == "__main__":
    main()

