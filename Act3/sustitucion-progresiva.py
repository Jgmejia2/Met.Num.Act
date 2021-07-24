import numpy as np

A = np.array([[6, 0, 0, 0.],
              [3, 6, 0, 0],
              [4, -2, 7, 0],
              [5, -3, 9, 21]])
b = np.array([12, -12, 14, -2])

def sustProgresiva(A,b):
    n=np.size(b)
    x = np.zeros(n)
    for i in range (n):
        sum = 0
        for p in range (i):
            sum += A[i,p]*x[p]
        x[i] = (b[i]-sum)/A[i,i]
    print()
    print("______SUSTITUCION PROGRESIVA______")
    print("SU VECTOR RESULTANTES ES: ",x)

sustProgresiva(A,b)