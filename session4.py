import numpy as np 
import sys 
#import sys and numpy

class MyPet(): #establishes class to describe the animal
    def __init__(self, arm_len, leg_len, eye_num, has_tail, is_fluffy):
        
        self.tail = has_tail #does it have a tail(bool)
        self.arm_length = arm_len #length of arms(float)
        self.leg_length = leg_len #length of legs(float)
        self.eye_number = eye_num #number of eyes(integer)
        self.fluffy = is_fluffy #is it fluffy(bool)
        
    def describe(self): '''member function of the class that prints out 
    and describes the data members representing the physical characteristics of the animal'''
        print("Your pet has a tail:", pet1.tail)
        print("Your pet's arm length is ", pet1.arm_length)
        print("Your pet's leg length is ", pet1.leg_length)
        print("The number of eyes your pet has is ", pet1.eye_number)
        print("Your pet is fluffy:", pet1.fluffy) 

#defines the attributes of my pet to print out
pet1 = MyPet(has_tail = True,arm_len = 6.0,leg_len = 6.0,eye_num = 2,is_fluffy = True)

#lists out the characteristics of my pet
pet1.describe()