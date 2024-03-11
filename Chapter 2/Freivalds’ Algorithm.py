import numpy as np
import galois
import random

def verify(A, B, C):
    n = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1], C.shape[0], C.shape[1])
    p = galois.next_prime(n**2) # Choose the prime to work with, the prime can be increased inorder to increase security

    A = A % p
    B = B % p
    C = C % p
    
    GFP = galois.GF(p) # Creating our prime field
    
    # Reconstricting the matrices in our prime field to be able to work on them
    AA = GFP(A)
    BB = GFP(B)
    CC = GFP(C)

    random_element = GFP(random.randint(0, p-1))
    X = [random_element ** i for i in range(n)]
    X = np.array(X) # Converting list to NumPy array if necessary
    X = GFP(X)

    left_side = CC @ X
    right_side = AA @ (BB @ X)
    return np.array_equal(left_side, right_side)


if __name__ == "__main__":

    # A and B is known by both parties
    A = np.array([[1, 2], [3, 4]]) 
    B = np.array([[1, 2], [3, 4]])
    # We assume C is sent by prover
    C = np.array([[7, 10], [15, 22]])

    result = verify(A,B,C)
    print(result)
