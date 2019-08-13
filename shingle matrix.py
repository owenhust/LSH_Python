##This is to convert the document number word number pair dataframe into shingle matrix (binary).
##input data frame of document number and word number pairs:
##1  1   20
##2  1   25
##3  1   36
##4  2   13
##5  2   36
##6  2   13
##.........
##the outcome 

from scipy.sparse import csr_matrix 
import numpy as np 

def shingle_mat(wordNum, docNum, pair_data):
	#build the shingle matrix using scipy sparse matrix package 
	shingle_mat = csr_matrix(np.zeros([wordNum,docNum]))

	for j in range(docNum):
		#document and word numbers start from 1 here, so there could + - 1 to adjust the indices.
		shingle_mat[pair_data.loc[pair_data.iloc[:,0]==j+1,1]-1,j] =1
	return shingle_mat