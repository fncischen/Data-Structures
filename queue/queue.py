class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(len(self.storage),item)
  
  def dequeue(self):
    if len(self.storage) != 0:
      return self.storage.pop(0)
    else:
      return None

  def len(self):
    return len(self.storage)

e = Queue()
e.enqueue(3)
e.enqueue(5)
e.enqueue(7)
print(e.len())
print(e.dequeue())