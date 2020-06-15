import numpy as np
import pandas as pd


#loading data from file
data = np.loadtxt("ex1data2.txt", comments="#", delimiter=",", unpack=False)

# load the first two columns into X
X = data[:, :2]
    
# load from the third column into y
y = data[:, 2]

g = X.shape[0]
print ( X[g-1])


f = open("ex1data2.txt" , "a+")
while True:  
    f.write("1650,3,0\n")
    if(g != 0):  
        break  
f.close()

f = open("ex1data2.txt" , "a+")
while True:  
    f.write("3000,4,0\n")
    if(g != 0):  
        break  
f.close()

hypothesis = 
