#initialize
A = [1,2,3,4,5,6]
B = [3,4,5,3,2,5]
C = [1]

#maintenance
for i in range(0,len(A)):
    C.append(A[i]+B[i])

#termination
print(C)
