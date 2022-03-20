'''
Author: Pashupati Shah
Licensed to : 
'''

### Comment
    #To write a comment:
    #use pound symbol in front of the line OR use '''   ''' like below
'''
    All the text inside ''' ''' is comment.

    Comments are bits of text in the program that the computer ignores. 
    `They are there solely for the benefit of any human readers.
    '''

### Inbuilt Functions
#Here we will use the following functions:
# print() 
# input()
# type()
# len() 
# min()
# max()

print("Hello World") #This function prints whatever is inside ()

#Welcome people
name = input("Enter your name: ") # This function asks for user input
print("Welcome to learn Python,", name)

print(type(2)) # This type() fnction gives the data type of number 2 which is inside ()
print(type(2.0)) 
print(min(4,3,2,5,6,7)) #This min() function calculate the minimum number from the list of number
print(max(4,3,2,5,6,7)) #This max() function calculate the maximum number from the list of number
#This is to show how to import modules
import os  #importing os module
import numpy as np #Import numpy module; Note numpy must be installed
import pandas as pd #Import pandas module; Note pandas mist be installed
