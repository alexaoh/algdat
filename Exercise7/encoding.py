"""Get coding of different letters from given Huffman-tree 

The Node()-object has attributes 'left_child' and 'right_child', 
which are none if the node has no children. Node() also has 
an attribute 'character' which is the letter that the node 
represents. These are in the leaves of the tree. 
"""

def encoding(node):
    """node is the root of the tree. Returns a dictionary 
    with the letters as keys and the binary value as values.
    """
    dicti = {}
    def fill_dict(node, dicti, current):
        if node.left_child == None:
            dicti[node.character] = current

        if node.left_child != None:
            fill_dict(node.left_child, dicti, current + "0")

        if node.right_child != None:
            fill_dict(node.right_child, dicti, current + "1")




    fill_dict(node, dicti, "")
    return dicti

