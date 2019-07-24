import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # first, append the item into the array
    self.storage.append(value)
    # second, check if the item is greater than the parent, begin swapping
    if self.storage[len(self.storage)-1] > self.storage[math.floor((len(self.storage)-1)/2)]:
      parentToSwap = self.storage[math.floor((len(self.storage)-1)/2)]
      self.storage[len(self.storage)-1], self.storage[math.floor((len(self.storage)-1)/2)] = parentToSwap, value 

  def delete(self):
    self.storage.pop(0)
    # next, compare the most bottom element to the former two children 
    lastItem = self.storage[len(self.storage-1)]
    self.storage.insert(0,lastItem)

    # check if the bottom element is greater than the left child
    if self.storage[0] < self.storage[1]:
       # if not, begin swapping WITH LEFT CHILD
       self.storage[0], self.storage[1] = self.storage[1], self.storage[0]
       swapping = True
       n = 1
       while swapping: 
         # check if the item at its new location is greater than its children
         # if it is not, continue swapping  
         if self.storage[n] < self.storage[2*n+1]:
            self.storage[n], self.storage[2*n+1] = self.storage[2*n+1], self.storage[n]
            n = 2*n + 1 
            swapping = True 
         elif self.storage[n] < self.storage[2*n+2]
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

       while swapping: 
      # check if the item at its new location is greater than its children
          if self.storage[n] < self.storage[2*n+1]:
            self.storage[n], self.storage[2*n+1] = self.storage[2*n+1], self.storage[n]
            n = 2*n + 1 
            swapping = True 
         elif self.storage[n] < self.storage[2*n+2]
            self.storage[n], self.storage[2*n+2] = self.storage[2*n+2], self.storage[n]
            n = 2*n + 2 
            swapping = True 
      # if it is not, continue swapping  
        swapping = False 

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
