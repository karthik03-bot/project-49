import numpy as np
A= np.array([(1,2,3),(7,8,9)])
print(A[1,2]) #Slicing concept 
print(A.max()) #to know max value using max() function
print(A.min()) #to know min value
print(A.sum()) # to know the sum of the 2d array 
print(np.sqrt(A)) # to know the square root of each value in function 
print(np.std(A)) #to standard deviation of the given array
B = np.array([(5,2,3),(7,8,1)])
print(np.hstack(A+B)) # adding two arrays matrix addition and using hstack function 
print(A-B) # subraction of two arrays 
print(np.exp(A)) #spacial functions in numpy exponential
print(np.log(B)) #spacial functions in numpy logerithemic
print(np.hstack(B)) #horizontal stacking on an array
print(np.size(A)) # shape() function is used to determine no.of (rows,columns)
print(np.shape(A)) # size() function is used to determine size of the array 
print(np.ndim(A)) # ndim() command is used for determine dimension of the array 
print(np.ravel(B)) # this ravel command is used for arranging the elements of array in order
