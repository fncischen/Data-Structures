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
      if self.right not None:
        self.right.insert(value)
      else:
    # if it does not exist, set the right tree equal to a new BST subtree with this value    
        self.right = BinarySearchTree(value)

  def contains(self, target):
    # check for three conditions

    # check if the target equals self value
    if target == self.value  
    # if so, return True
      return True
    
    # if not, check and see if the target is less than or equal to the target
    if target < self.value:
      # if so, search in the left subtree
      if self.left not None:
        self.left.contains(target)
      # if the left subtree does not exist return False
      else:
        return False
    
    else:
      # if not, search on the right subtree
      if self.right not None:
        self.right.contains(target)
      # if the right subtree does not exist, return False 
      else:
        return False 

  def get_max(self):
    # first set a max value // assume a sorted BST 
      max = self.value 
      
    # start at an initial node right
      right = self.right 

    # traversing the right tree until there is no right node 
      while right:
        max = right.value 
        right = right.self.right 

      return max 

    pass

  def for_each(self, cb):
    pass

# 

# 8
# 3 10 (left is always smaller than right)