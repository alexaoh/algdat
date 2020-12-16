def longest_decreasing_subsequence(s):
    # Trying to follow the same pattern as in LCS
    # Make an array of descending number from max to 1 (dec)
    # This makes the rows of the table.
    # Compare each entry with the sequence s (in the columns) 
    # and fill out the table c.
    # To reconstruct the solution, the table b is also used. 
    
    m = max(s)
    dec = [i for i in range(m, 0, -1)]
    d = len(s)
    c = [[0 for x in range(d)] for y in range(m)]  # Table to store bottom up solution.
    b = [[0 for x in range(d)] for y in range(m)]  # Table to store choices taken. 
    for row in range(m):
        for col in range(d):
            if s[col] == dec[row]:
                c[row][col] += 1
                b[row][col] = "-"
                if row > 0 and c[row-1][col] != 0:
                    c[row][col] += c[row-1][col]
                    
            if col > 0 and c[row][col-1] != 0:
                c[row][col] = c[row][col-1]
    
    # From b and c, need to fint the longest decreasing subsequence.
    maximum_length = max(map(max, c)) # This is the maximum length.

    # Find the starting indices of the maximum length.
    row_index = list(map(max, c)).index(maximum_length)
    col_index = c[row_index].index(max(c[row_index]))
    
    lcs = []
    # Now, traverse b back towards the top right. 
    for row in range(row_index, -1, -1):
        for col in range(col_index, -1, -1):
            if b[row][col] == "-":
                lcs.append(s[col])
                break
            
    return lcs[::-1] # Reverse the list before returning. 
    
