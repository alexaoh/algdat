def counting_sort(A, B):
    n = len(A)
    
    if n != 0:
        k = max(A)
    else: 
        return 
    
    C = [0]*(k+1)
    for i in range(n):
        C[A[i]] += 1 # Count the values in A in the correct indices in C.
    
    # Make cumulative C.
    for i in range(1, k+1):
        C[i] += C[i-1]
    
    # Sort the array and output to B.
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i] 
        C[A[i]] -= 1

