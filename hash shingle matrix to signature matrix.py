##This algorithm is based on section 3.3 in Mining of Massive Datasets by Jure Leskovec, etc.  
##The function is designed to transform shingle matrix with 1 for document containing word, 0 for not, 
##to signature matrix based 
import numpy as np

def hash_sign(d,shingle_mat):
	#initilise the signature matrix 
	sign_mat = np.matrix(np.ones([d,docNum]) * np.inf)
    
	#randomly generate list with values lower than wordNum
	hash_row = np.zeros([d,wordNum])
	for i in range(d):
		hash_coef = [random.choice(list(range(1,wordNum))),random.choice(list(range(1,wordNum)))]
		
		#store hash values in matrix of d x wordNum (row in the course slides)
		#call hash_func to calculate the hash function values based on random generated coefficients
		hash_row[i,:]=hash_func(hash_coef)
        
	#generating the signature matrix        
	for i in range(wordNum):
		 
		one_column = np.squeeze(np.asarray(shingle_mat[i,:].todense()==1))
		
		if any(one_column):
			for j in range(d):
				indices = np.squeeze(np.asarray(hash_row[j,i] < sign_mat[j,:])) & one_column
				sign_mat[j,indices] = hash_row[j,i]
	return sign_mat 
	
def hash_func(hash_coeff):
	#a universal hash function: ((a*x + b) mod p mod docNum), where p is a large prime > docNum
	#and 0 < a, b < docNum; this double mods can reduce the collison probability for large number 
	#of hash functions 
	
	a = hash_coeff[0]
	b = hash_coeff[1]
	
	#everytime calculate 0 to wordNum row for each hash function
	return (a*np.array(list(range(wordNum)))+b)% find_next_prime() % wordNum    #see seperate file find_next_prime
