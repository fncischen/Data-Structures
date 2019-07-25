import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # first, append the item into the array
    self.storage.append(value)
    # second, check if the item is greater than the parent, begin swapping

    # print("Index", len(self.storage)-1)
    # print("Parent index", math.floor((len(self.storage)-1)/2))
    # print("Storage", self.storage)

    lastIndex = len(self.storage)-1
    parentIndex = math.floor((lastIndex-1)/2)
    # print("Testing")
    # print("lastIndex:", lastIndex)
    # print("parentIndex:", parentIndex)

    swapping = True   

    while swapping:
      swapping = False
      if self.storage[lastIndex] > self.storage[parentIndex]:
        # print("Swapping")
        parentToSwap = self.storage[parentIndex]
        self.storage[lastIndex], self.storage[parentIndex] = parentToSwap, value 
        
        lastIndex = parentIndex
        parentIndex = math.floor((lastIndex-1)/2)
        # print("lastIndex changed:", lastIndex)
        # print("parentIndex changed:", parentIndex)

        if parentIndex >= 0:
          swapping = True

  def delete(self):
    print("Before self storage", self.storage)
    self.storage.pop(0)
    # next, compare the most bottom element to the former two children 
    # print("Self storage", self.storage)
    # print(len(self.storage))
    lastItem = self.storage[len(self.storage)-1]
    # print("last item:", lastItem)
    self.storage.pop(len(self.storage)-1)
    self.storage.insert(0,lastItem)
    # print("Self storage modifed", self.storage)

    # check if the bottom element is greater than the left child
    if len(self.storage) > 2:
      if self.storage[0] < self.storage[1]:
        # if not, begin swapping WITH LEFT CHILD
        self.storage[0], self.storage[1] = self.storage[1], self.storage[0]
        swapping = True
        n = 1
        while swapping & (2*n+1) > len(self.storage) - 1: 
          # check if the item at its new location is greater than its children
          # if it is not, continue swapping  
            print("We are at node", n)
            print("Check", self.storage)
            if self.storage[n] < self.storage[2*n+1]:
                self.storage[n], self.storage[2*n+1] = self.storage[2*n+1], self.storage[n]
                n = 2*n + 1 
                swapping = True 
            elif self.storage[n] < self.storage[2*n+2]:
                self.storage[n], self.storage[2*n+2] = self.storage[2*n+2], self.storage[n]
                n = 2*n + 2 
                swapping = True 
            
            swapping = False 
 
      # check if the bottom element is greater than the right child
      elif self.storage[0] < self.storage[2]:
        # if not, begin swapping WITH RIGHT CHILD
        self.storage[0], self.storage[2] = self.storage[2], self.storage[0]
        swapping = True
        n = 2

        while swapping and (2*n+1) > len(self.storage) - 1: 
        # check if the item at its new location is greater than its children
          if self.storage[n] < self.storage[2*n+1]:
              self.storage[n], self.storage[2*n+1] = self.storage[2*n+1], self.storage[n]
              n = 2*n + 1 
              swapping = True 
          elif self.storage[n] < self.storage[2*n+2]:
              self.storage[n], self.storage[2*n+2] = self.storage[2*n+2], self.storage[n]
              n = 2*n + 2 
              swapping = True 
        # if it is not, continue swapping  
          swapping = False 

      print("Final self storage", self.storage) 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    self.storage[index], self.storage[math.floor(index/2)] = self.storage[math.floor(index/2)], self.storage[index]

  def _sift_down(self, index):
    if self.storage[index] < self.storage[2*index+1]:
      self.storage[index], self.storage[2*index+1] = self.storage[2*index+1], self.storage[index]
    elif self.storage[index] < self.storage[2*index+2]:
      self.storage[index], self.storage[2*index+2] = self.storage[2*index+2], self.storage[index]

# heap = Heap()

# heap.insert(6)
# heap.insert(8)
# print(heap.storage)
# heap.insert(10)
# heap.insert(9)
# heap.insert(15)

# print(heap.storage)

# heap.delete()
# heap.delete()
# heap.delete()
# heap.delete()
# print(heap.storage)