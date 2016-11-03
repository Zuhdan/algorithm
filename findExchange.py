A = [56,43,23,41,22,13]
keep = A[0]

for i in range(0,len(A)):
    if keep > A[i]:
        keep = A[i]
    print (keep)
