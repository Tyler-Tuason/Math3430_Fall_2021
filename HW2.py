#Problem #1
"""""""
Write an algorithm to implement scalar-vector multiplication.
Q1: a scalar and a vector stored as a list. named Scalar_1 and Vector_1 respectively.
Q2: store their product as a new list
Q3:  we will create an empty list with the same size as vector_1. we will then store the product of vector_1 and scalar_1 in the empty list

def MultiplyVectorbyScalar(Scalar_1,Vector_1):
# setting result as an empty list

  Vector_1 = {}
  for index in range((len(Vector_1)):
    result.append(0)
# the scalar is multiplied to each number of the vector then replaced with the product.

  Return Result
# Retrieve the new vector
"""""""
def MultiplyVectorbyScalar(Scalar_1,Vector_1):
  Vector_1 = {}
  for index in range((len(Vector_1)):
    result.append(0)
  Return Result
                     
# MultiplyVectorbyScalar(test_vector_1,test_Scalar_1) should output [2,4,6]
print('Test Output for multiplyVectorbyscalar: ' + str(MultiplyVectorbyScalar(test_vector_1,test_Scalar_1)))
print('Should have been [2,4,6]')
                     
# MultiplyVectorbyScalar(test_vector_2,test_Scalar_1) should output [4,8,12]
print('Test Output for multiplyVectorbyscalar: ' + str(MultiplyVectorbyScalar(test_vector_2,test_Scalar_1)))
print('Should have been [4,8,12]')
  
""""""
#Problem #2
""""""
Write an algorithm to implement scalar-matrix multiplication.
Q1: a scalar named Scalar_1 and a matrix named Matrix_1 stored as a list
Q2: a matrix which is the scaled version of given matrix
Q3: we will create an empty list for Matrix_1. we will then store the product of Matrix_1 and scalar_1 in the empty list.

def MultiplyMatrixbyscalar(Matrix_1,Vector_1)
# setting result as an empty list

  Matrix_1 = {}

  for index in range((len(matrix_1)):
    result.append(0)
# the scalar is multiplied to each number of the matrix then replaced with the product.

  NewMat = Scalar_1 * Matrix_1
  Return Result
# Retrieve the new vector

"""""""
 MultiplyMatrixbyScalar(Scalar_1,Matrix_1):
  Matrix_1 = {}
  for index in range((len(matrix_1)):
      result.append(0)
  NewMat = Scalar_1 * Matrix_1
  Return Result
                     
# MultiplyMatrixbyScalar(test_Matrix_1,test_Scalar_1) should output [[2,4,6],[4,8,12],[2,6,10]]
print('Test Output for multiplyMatrixbyscalar: ' + str(MultiplyMatrixbyScalar(test_Matrix_1,test_Scalar_1)))
print('Should have been [[2,4,6],[4,8,12],[2,6,10]]')

# MultiplyMatrixbyScalar(test_Matrix_2,test_Scalar_1) should output [[2,6,10],[4,8,12],[2,4,6]]
print('Test Output for multiplyMatrixbyscalar: ' + str(MultiplyMatrixbyScalar(test_Matrix_2,test_Scalar_1)))
print('Should have been [[2,6,10],[4,8,12],[2,4,6]]')
                     
""""
#Problem #3
""""
Write an algorithm to implement matrix addition.
Q1: two matrices stored as a list of lists, where each list represents a column. these matrices are called: Matrix_1 and Matrix_2.
Q2: store their sum as a new list
Q3: we will create an empty list for Matrix_1. we will then store the sum of Matrix_1 and Matrix_2 into the empty list. all assuming the matrices are of the same size.

def add_Matrices(matrix_1,Matrix_2)
# setting result as an empty list

  Matrix_1={}

  for index in range((len(matrix_1)):
   result.append(add_vectors(matrix_1[index],Matrix_2[Index])
# the matrix is added to each number of the matrix then replaced with the product.

  Return Result
# Retrieve the new vector

def add_Matrices(matrix_1,Matrix_2)
  Matrix_1 = {}
  for index in range((len(matrix_1)):
   result.append(add_vectors(matrix_1[index],Matrix_2[Index])
  Return Result
                 
# Add Matrices(test_Matrix_1,test_Matrix_2) should output [2,5,8],[4,8,12],[2,5,8]
print('Test Output for add_Matrices: ' + str(Add_Matrices(test_Matrix_1,test_Matrix_2)))
print('Should have been [2,5,8],[4,8,12],[2,5,8]')
                 
# Add Matrices(test_Matrix_2,test_Matrix_3) should output [2,6,10],[3,6,9],[3,6,9]
print('Test Output for add_Matrices: ' + str(Add_Matrices(test_Matrix_2,test_Matrix_3)))
print('Should have been [2,6,10],[3,6,9],[3,6,9]')
                 
#Problem #4

""""
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
problem #1.
Q1: A Matrix named Matrix_1 where each component list represents a column of the matrix and a vector stored as a list named vector_1.
Q2: store their product as a new list
Q3: we will initialize a result matrix. the for each component of result, we will overwrite it with the output

def MultiplyMatrixbyVector(Matrix_1,Vector_1)
  Matrix_1={}
  for element in Matrix_1
    Matresult.append(0)
  NewMat = Matrix_1 * Vector_1
  for index in range(length(result)):
  result[index] = Matrix_1[index] + vector_1[index]
Return Result

""""""
#Problem #5
""""""
Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.
Q1:two matrices stored as a list of lists, where each component represents a column. these are named Matrix_1 and Matrix_2
Q2:store their product as a new list
Q3:we will initialize a result matrix. then for each component of result, we will overwrite it with the output


def MultiplyMatrixbyMatrix(Matrix_1, Vector_2)
Matrix_1 = {}
for element in Matrix_1
  Matresult.append(0)
NewMat = Matrix_1 * Matrix_2
for index in range(length(result)):
  result[index] = Matrix_1[index] + Matrix_2[index]
  Return result
""""""
def MultiplyVectorbyScalar(Scalar_1,Vector_1):
  Vector_1 = {}
  for element in Vector_1:
      Vecresult.append(0)
  NewVec = Scalar_1 * Vector_1
  NewVec = Scalar_1 * Vector_1
  Return result
"""""
#Test_Inputs              
                 
Test_Vector_1 = [1,2,3]
Test_Vector_2 = [2,4,6]
Test_Vector_3 = [1,3,5]
Test_Scalar_1 = [2]

Test_Matrix_1 =[Test_Vector_1,Test_Vector_2,Test_Vector_3]
Test_Matrix_2 =[Test_Vector_3,Test_Vector_2,Test_Vector_1]
Test_Matrix_2 =[Test_Vector_3,Test_Vector_1,Test_Vector_2]
