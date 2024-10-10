import numpy as np 
import sys 

#define the base function in which we will plug x into
def f(x):
    return x**3 + 8

#define the variable x in f(x)
def main():
    x=9 
    result = f(x) #the result of plugging in 9 in for x in f(x)
    print("Result=", result) #The output of the function will be displayed
    
    if result > 27:
        print("YAY!") #if successfully greater than 27, then the program will print YAY!

if __name__ == "__main__":
    main()