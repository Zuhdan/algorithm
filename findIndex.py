A = [2,3,5,6,7,8,3,1]
S = 4
C = 0

for i in range(0,len(A)):
    if A[i] == S:
        C = 1;
        print(i)
    
if C == 0:
    print("No Value")
