def search_tree(root, dna):
    """Search for a dna sequence in the given tree."""
    i = 0
    while i < len(dna):
        if not dna[i] in root.children:
            return 0
        root = root.children[dna[i]]
        i += 1
    return root.count
