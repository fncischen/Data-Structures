"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head != None and self.tail != None:
      next = self.head
      self.head.insert_before(value)
      self.head = self.head.prev
      self.head.next = next 
      self.length += 1
    else: 
      NewNode = ListNode(value)
      self.head = NewNode
      self.tail = NewNode 
      self.length += 1

  def remove_from_head(self):
    value = self.head.value 
    if self.head == self.tail:
      self.head.delete()
      self.tail.delete()
      self.head = None
      self.tail = None 
      self.length -= 1 
      return value
    else:
      self.head.delete()
      self.length -= 1 
      return value 

  def add_to_tail(self, value):
    if self.head != None and self.tail != None:
      prev = self.tail 
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.tail.prev = prev 
      self.length += 1
    else: 
      NewTail = ListNode(value)
      self.tail = NewTail
      self.head = NewTail[]
      self.length += 1

  def remove_from_tail(self):
    value = self.tail.value
    if self.head == self.tail:
      self.head.delete()
      self.tail.delete()
      self.head = None
      self.tail = None 
      self.length -= 1 
      return value
    else: 
      self.tail.delete()
      self.length -= 1
      return value

  def move_to_front(self, node):
    # check and see if node is in the list
    currentSelectedNode = self.head
    while currentSelectedNode != None:
      if currentSelectedNode == node:
        currentSelectedNode.delete()
        self.length -= 1 
        self.add_to_head(node.value)
        return self.head.value
      else:
        currentSelectedNode = currentSelectedNode.next

    print("We cannot find this node")


  def move_to_end(self, node):
    currentSelectedNode = self.head
    while currentSelectedNode != None:
      if currentSelectedNode == node:
        currentSelectedNode.delete()
        self.length -= 1 
        self.add_to_tail(node.value)
        return self.tail.value
      else:
        currentSelectedNode = currentSelectedNode.next

    print("We cannot find this node")

  def delete(self, node):
    currentSelectedNode = self.head
    while currentSelectedNode != None:
      if currentSelectedNode == node: 
        currentSelectedNode.delete()
        self.length -= 1
        break 
      else:
        currentSelectedNode = currentSelectedNode.next


  def get_max(self):
    max = self.head.value 
    currentSelectedNode = self.head
    while currentSelectedNode != None:
      if currentSelectedNode.value > max:
        max = currentSelectedNode.value 
      else:
        currentSelectedNode = currentSelectedNode.next

    return max 

# 10 5 7
# 10 7 5

g = ListNode(5)
e = DoublyLinkedList(g)
e.add_to_tail(7)
e.add_to_head(10)
e.move_to_end(g)

print(e.head.value)
print(e.head.next.value)
print(e.tail.value)

print(e.length)