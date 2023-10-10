import numpy as np

twoDArray = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ])
print(twoDArray)

# newTwodArray = np.insert(twoDArray, 0 ,[[1,2,3,4]], axis=0)
# print(newTwodArray)

# def accessElemets(array, rowIndex, colIndex):
#     if rowIndex >=len(array) and colIndex >= len(array[0]):
#         print("Incorrect index")
#     else:
#         print(array[rowIndex][colIndex])

# accessElemets(twoDArray,1,2)


# def traverseTwoDArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])

# traverseTwoDArray(twoDArray)            

# def searchTDArray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return 'The element is located at index '+str(i)+" "+str(j)
#     return "The element is not found"

# print(searchTDArray(twoDArray,223))

newTDArray = np.delete(twoDArray, 0 ,axis=0)
print(newTDArray)