import random
# recursively try to insert key,data pair into tree at cur.
# Return the modified tree.
def __rinsert(self, cur, k, d):
    if not cur:    # empty tree, so just insert the node
        self.__size += 1
        return Node(k, d)
    
    # insert k,d in the left or right branch as appropriate
    if k < cur.key: 
        cur.leftChild  = self.__rinsert(cur.leftChild,  k, d)
        
    elif k > cur.key: 
        cur.rightChild = self.__rinsert(cur.rightChild, k, d)
     
    # at this point, k,d was inserted into the correct branch,
    # or it wasn't inserted since the key k was already there
    return cur

def main():
    for i in range(15):
        r = random.random()
        print(r)
        
        
main()