import numpy as np 
import sys 
import math as m 

def sin_table(start, end, num_entries): #generates x values and their sin vales
    x_values = []
    sin_values = []
    step = (end - start) / (num_entries - 1)
    
    for i in range (num_entries):
        x= start + i * step
        sin_x = m.sin(x)
        x_values.append(x)
        sin_values.append(sin_x)
        
    return x_values, sin_values

def print_table(x_values, sin_values): #makes the table with formatting
    print(f"{'x':<10} {'sin(x)':10}")
    print("-" * 20)
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x:<10.4f} {sin_x:<10.4f}")
        
def main(): #sets up the parameters and calls the functions 
    start = 0 
    end = 2 * np.pi
    num_entries = 1000
    x_values, sin_values = sin_table(start, end, num_entries)
    print_table(x_values, sin_values)
    #the first column lists the x values incrementing from 0 to approx 2 pi
    #the second column lists the corresponding sin values according to the x value
if __name__ == "__main__":
    main()