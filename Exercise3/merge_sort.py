def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    
    # Copy the values into two new arrays.
    for i in range(n1):
        L[i] = a[p + i]
    for i in range(n2):
        R[i] = a[q + 1 + i]
    
    i = 0
    j = 0
    k = p

    # Don't have sentinel value, so need to do some extra work here.
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # Copy remaining values (only one of the loops will run)
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


def merge_sort(a, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)
        