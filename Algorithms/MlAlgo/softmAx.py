import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    resA=[0]*len(L)
    sumE=0
    for x in L:
        sumE+=np.exp(x)
    for i in range(len(L)):
        resA[i]=np.exp(L[i])/sumE


    return resA