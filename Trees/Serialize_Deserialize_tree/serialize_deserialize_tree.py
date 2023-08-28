# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # we serialize by adding the nodes in a array and each time the direction of edge changes 
        # between left or right (when the node hits a None ptr) then we add a # to separate them by level
        # We add the encoded strings into array and return into
        # we traverse through the tree in a preorder traversal
        rc = []

        def encodeNode(node):
            if not node:
                rc.append("#")
                return None
            
            rc.append(str(node.val))
            encodeNode(node.left)
            encodeNode(node.right)
        encodeNode(root)
        return "|".join(rc)
            


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Deserialize the same way we serialized the tree
        data = data.split("|")

        def decodeArr():
            if data:
                nodeVal = data.pop(0)

                if nodeVal == "#":
                    return None
                else:
                    root = TreeNode(nodeVal)
                    root.left = decodeArr()
                    root.right = decodeArr()

                return root

        return decodeArr()
