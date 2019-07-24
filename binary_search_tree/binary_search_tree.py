import random

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # check if the value is less than or equal to the value on top
    # if less than, traverse to the left
    if value < self.value:

    # check if a left tree exists, if so, traverse from the top to bottom     
    # by accessing the left tree and searching for an empty tree
      if self.left != None:
        self.left.insert(value)
      else:
    # if it does not exist, set the left tree equal to a new BST subtree with this value
        self.left = BinarySearchTree(value)

    else:
    # if greater than, traverse to the right

    # check if a right tree exist; if so, traverse from the top to the bottom
    # by accessign the right tree and searching for an empty tree
      if self.right != None:
        self.right.insert(value)
      else:
    # if it does not exist, set the right tree equal to a new BST subtree with this value    
        self.right = BinarySearchTree(value)

  def contains(self, target):
    # check for three conditions

    # check if the target equals self value
    print("Our target:", target)
    print("Our value", self.value)
    if target == self.value:  
        print("Yes it exists!")
        return True
    else: 
    # if not, check and see if the target is less than or equal to the target
      if target < self.value:
        # if so, search in the left subtree
        if self.left != None:
          return self.left.contains(target)
        # if the left subtree does not exist return False
        else:
          print("It does not exist")
          return False
      
      else:
        # if not, search on the right subtree
        if self.right != None:
          return self.right.contains(target)
        # if the right subtree does not exist, return False 
        else:
          print("It does not exist")
          return False 

  def get_max(self):
    # first set a max value // assume a sorted BST 
      max = self.value 
      
    # start at an initial node right
      right = self.right 

    # traversing the right tree until there is no right node 
      while right:
        max = right.value 
        right = right.right 

      return max 


# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# depth first or breadth search 
  def for_each(self, cb):

    # breadth traversal
    root = self.value
    left = self.left 
    right = self.right 
    
    print("What is root", root)
    print(left)

    # set up an iterator of levels to loop through 
    levels = []
    levels.append(left)
    levels.append(right)



    # apply callback function to root
    cb(root) 

    # assume no empty levels 
    noEmptyLevels = False 

    while not noEmptyLevels:
      noEmptyLevels = True 
     
    # apply the callback function on the values of each BST

      for level in levels:
          if level:
            cb(level.value)
        
    # replace the BST subtrees with new subtrees by looping through
    # the levels subtree

      oldlevels = levels
      levels = []
      for level in oldlevels:
        if level: 
          if level.left:
            levels.append(level.left)
          if level.right: 
            levels.append(level.right)
      
    # what condition to check -? if ALL the level BST left and right are equal to None - let the while loop know
      if len(levels) > 0:
        noEmptyLevels = False 
    
    # else: 
    # continue this sequence until the tree has no more roots to loop through

bst = BinarySearchTree(5)
# bst.insert(2)
# bst.insert(3)
# bst.insert(7)
# bst.insert(6)
# bst.insert(2)
# bst.insert(3)
# bst.insert(7)
# print(bst.contains(7))
# print(bst.contains(8))

arr = []
cb = lambda x: arr.append(x)

v1 = random.randint(1, 101)
v2 = random.randint(1, 101)
v3 = random.randint(1, 101)
v4 = random.randint(1, 101)
v5 = random.randint(1, 101)

print(v1)
print(v2)

bst.insert(v1)
bst.insert(v2)
bst.insert(v3)
bst.insert(v4)
bst.insert(v5)

# print("Check", bst.contains(v1))

bst.for_each(cb)

print(arr)