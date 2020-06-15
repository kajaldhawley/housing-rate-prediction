import numpy as np

def calculate_hypothesis(X, theta, i):
    """
        :param X            : 2D array of our dataset
        :param theta        : 1D array of the trainable parameters
        :param i            : scalar, index of current training sample's row
    """
    hypothesis = 0.0
    #########################################

    #hypothesis = np.dot(X, theta , axis = 1)
     #hypothesis 
    
    m = len(theta)
    for j in range (0 , m):
    	hypothesis +=  X[i , j] * theta[j]
        
				
    
    ########################################/
    
    return hypothesis
