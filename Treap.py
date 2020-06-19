import random

class Node(object):
    # create a treap node consisting of a key/data pair and a priority
    def __init__(self, k, d, p=0):
        self.key  = k
        self.data = d
        # priority is 0 unless othewise specified
        # (for some reason the random module isn't working properly)
        self.priority = p
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return "{" + str(self.key) + ", " + str(self.data) + " [" + str(self.priority) + "]" + "}"

class Treap(object):
    # create empty treap
    def __init__(self):
        self.__root = None
        self.__size = 0
    
    # recursively tries to find node with key k, starting at node n.
    # returns node if found, otherwise returns parent.
    # used for find, insert, and delete
    def __rfind(self, k, n):
        
        # if n doesn't exist, don't even bother
        if not n: return None
        
        # recursively search into left or right branch
        if n.leftChild and k < n.key: return self.__rfind(k, n.leftChild)
        if n.rightChild and k > n.key: return self.__rfind(k, n.rightChild)
        
        # if node with key k was found, return it
        # otherwise, return leaf that would be its parent
        return n
    
    # wrapper find function.
    # calls rfind on a key and returns associated data if found (None otherwise)
    def find(self, k): 
        cur = self.__rfind(k, self.__root)
        if cur and cur.key == k: return cur.data
        else: return None
        
    # wrapper insert function.
    # calls rfind on a key, and does nothing if key exists
    # otherwise, it adds a child to the leaf and rotates it up until heap condition is satisfied
    def insert(self, k, d, p=0):
        # create new node
        n = Node(k, d, p)
                
        # figure out where to put it with modified find function
        cur = self.__rfind(k, self.__root)
        
        # if treap is empty, set root to point to n and increment __size
        if not cur:
            self.__root = n
            self.__size += 1
            return
        # if key already exists, do nothing
        if cur.key == k: return
        # otherwise, insert it at appropriate place and increment __size
        if k < cur.key: cur.leftChild = n
        if k > cur.key: cur.rightChild = n
        self.__size += 1
        
        # trickle up
        self.__heapify(self.__root)
        
      
    def rotateRight(self, cur):
        tmp = cur.leftChild
        cur.leftChild = tmp.rightChild
        tmp.rightChild = cur
        return tmp
    
    def rotateLeft(self, cur):
        tmp  = cur.rightChild
        cur.rightChild = tmp.leftChild
        tmp.leftChild  = cur
        return tmp    
    
    # function that rotates subtrees if they don't satisfy minheap condition.
    # If priority of child is less than that of parent, rotate around parent
    def __heapify(self, cur):
        if not cur: return
        if cur.leftChild:
            if cur.leftChild.priority < cur.priority:
                cur = self.rotateRight(cur)
            self.__heapify(cur.leftChild)
            
        if cur.rightChild:
            if cur.rightChild.priority < cur.priority:
                cur = self.rotateLeft(cur)
            self.__heapify(cur.rightChild) 
            
    # delete a node with key k by rotating it down until it is a leaf.
    # TODO: fix this?
    def delete(self, k):
        # cur will be the node to be deleted, and prev is its parent
        cur = self.__root
        prev = None
        # loop through treap (non-recursively) and update prev and cur
        # until cur points to the node to be deleted
        while cur and cur.key != k:
            prev = cur
            if k < cur.key: cur = cur.leftChild
            if k > cur.key: cur = cur.rightChild
        
        # rotate cur down until it is a leaf and update prev accordingly
        # also, keep track of whether cur is to the left or right of prev
        # True means right, False means left
        c = True
        while cur.rightChild or cur.leftChild:
            if cur.leftChild:
                c = True
                prev = self.rotateRight(cur)
            else:
                c = False
                prev = self.rotateLeft(cur)
                
        # snip off cur using the tracker, and reheap the treap
        if prev:
            if c: prev.rightChild = None
            else: prev.leftChild = None
            self.__heapify(self.__root)
        # if prev is still none after all this, cur was the only node
        else: self.__root = None
        
        self.__size -= 1

###
        
    def getSize(self):
        return self.__size
    
    def preOrder(self, cur):
        if cur:
            print(" " + str(cur), end="")
            self.preOrder(cur.leftChild)
            self.preOrder(cur.rightChild)
      
    def inOrder(self, cur):
        if cur:
            self.inOrder(cur.leftChild)
            print(" " + str(cur), end="")
            self.inOrder(cur.rightChild)

    def postOrder(self, cur):
        if cur:
            self.postOrder(cur.leftChild)
            self.postOrder(cur.rightChild)
            print(" " + str(cur), end="")
            
    def traverse(self, traverseType):
        print(traverseType + "order traversal: ", end="")
        if traverseType == "pre":  self.preOrder(self.__root)
        elif traverseType == "in": self.inOrder(self.__root)
        else:                      self.postOrder(self.__root)
        print()  
    
    def printTree(self):
        self.pTree(self.__root, "ROOT:  ", "")
        print()
        
    def pTree(self, n, kind, indent):
        print("\n" + indent + kind, end="")
        if n: 
            print(n, end="")
            if n.leftChild:
                self.pTree(n.leftChild,  "LEFT:   ",  indent + "    ")
            if n.rightChild:
                self.pTree(n.rightChild, "RIGHT:  ", indent + "    ")

# ????????????????????????
def __main():
    t = Treap()
    nodes = [[0, 1], [1, 2], [9, 4], [8, 5], [0, 9], [2, 1], [3, 2]]
    for i in range(len(nodes)):
        print(nodes[i])
        t.insert(nodes[i][0], i, nodes[i][1])
        t.printTree()
    t.delete(9)
    t.printTree()
    
if __name__ == '__main__':
    __main()  