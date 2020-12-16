def build_tree(dna_sequences):
    i = 0
    root = Node() # Make empty Node object (predefined).

    while i < len(dna_sequences):
        #copy = root # Copy the node such that it can be used to traverse the tree.
        # Not sure about shallow/deep copy problems here.
        if dna_sequences[i] == "":
            root.count += 1
        for letter in dna_sequences[i]:
            if not letter in root.children:
                print("her")
                root.children[letter] = Node()
                root.children[letter].count += 1
                print(root)
            else:
                print("herda")
                root.children[letter].count += 1
            #root = root.children[letter] # Move the copy downwards in the tree.
            
            # I am missing a way to traverse the tree downwards with a node (always beginnning from the node)
            # This is what I tried to do, but I do not think it worked with copy!
            # I think this is pretty close to a solution however (hopefully!)
        i += 1

    return root

