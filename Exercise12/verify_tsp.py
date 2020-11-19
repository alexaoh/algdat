def verify_tsp(path, max_weight, weight_matrix):
    """Verification algorithm for the travelling salesman problem (TSP)."""
    s = 0
    for i in range(len(path)-1):
        w = weight_matrix[path[i]][path[i+1]]
        if w == 0:
            return False
        s += w
    if path[0] == path[-1] and s <= max_weight:
        return True
    return False

