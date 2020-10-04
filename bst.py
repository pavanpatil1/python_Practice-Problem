
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
    
def insert(root,node): 
        l1=[ord(c) for c in root.val]   
        l2=[ord(c) for c in node.val]
        if root is None: 
            root = node 
        else: 
            if l1 < l2: 
                if root.right is None: 
                    root.right = node 
                else: 
                    insert(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = node 
                else: 
                    insert(root.left, node) 
                    
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)

def deletenode(root,k):
    if root is None:
        return root

    if k < root.val:
        root.left = deletenode(root.left,k)

    if k > root.val:
        root.right = deletenode(root.right,k)     

def searchelement(root,k):

    if root is None:
        return root

    if root.val < k:
        root.right = searchelement(root.right,k)

    if root.val > k:
        root.left = searchelement(root.left,k)        

root=raw_input("Enter Root Element:\t")
def main():
    global key
    r = Node(root)
    while True:
        print "-"*50
        print "Binary Search Dictionary"
        print "1.Insert Element"
        print "2.Show Tree"
        print "3.Delete Element"
        print "4.Search Element"
        print "5.Exit"
        print "-"*50
        ch=input("Enter Your Choice")
        if ch==1:
            val=raw_input("Enter Word to be inserted:\t")
        
            insert(r,Node(val))
        
        if ch==2:
            print "Your Tree in INORDER :\n"
            inorder(r)

        if ch==3:
            d = raw_input("Enter The Word to delete")
            deletenode(r,Node(d) )  

        if ch==4:
            l = raw_input("Enter The Element to search")
            searchelement(r,Node(l))
        if ch==5:
            print ("Thank You")
            break     

if __name__=='__main__':
    main()