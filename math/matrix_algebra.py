# Matrix Algebra

import numpy as np

A = np.array([(1,2,3),(2,7,4)])

B = np.array([(1,-1),(0,1)])

C = np.array([(5,-1),(9,1),(6,0)])

D = np.array([(3,-2,-1),(1,2,3)])

u = np.array([6,2,-3,5])

v = np.array([3,5,-1,4])

w = np.array([(1,8,0,5)]).T

a = 6

# Dimensions
# 1.1 A
print(A.shape)

# 1.2 B
print(B.shape)

# 1.3 C
print(C.shape)

# 1.4 D
print(D.shape)

# 1.5 u
print(u.shape)

# 1.6 v
print(v.shape)

# Vector Operations
# 2.1
print(u+v)
# 2.2
print(u-v)
# 2.3
print(a*u)
# 2.4
print(np.dot(u,v))
# 2.5
print(np.sqrt(np.dot(u,u)))

# Matrix Operations
# 3.2
print(A-C.T)
# 3.3
print(C.T + 3*D)
# 3.4
print(np.dot(B,A))

# Optional
# 3.7
print(np.dot(C,B))
# 3.8
B2 = np.dot(B,B)
print(np.dot(B2,B2))
# 3.9
print(np.dot(A,A.T))
# 3.10
print(np.mat(D.T)*np.mat(D))
