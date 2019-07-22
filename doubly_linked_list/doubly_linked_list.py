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
    self.head.insert_before(value)

  def remove_from_head(self):
    self.head = self.head.next
    self.head.prev.delete()
    return self.head 

  def add_to_tail(self, value):
    self.tail.insert_after(value)

  def remove_from_tail(self):
   self.tail = self.tail.prev
   self.tail.next.delete()
   return self.tail 

  def move_to_front(self, node):
    # check and see if node is in the list
    currentSelectedNode = self.head
    while currentSelectedNode != self.tail:
      if currentSelectedNode == node:
        currentSelectedNode.delete()
        self.add_to_head(node)
        return self.head.value
      else:
        currentSelectedNode = currentSelectedNode.next

    print("We cannot find this node")


  def move_to_end(self, node):
    currentSelectedNode = self.head
    while currentSelectedNode != self.tail:
      if currentSelectedNode == node:
        currentSelectedNode.delete()
        self.add_to_tail(node)
        return self.tail.value
      else:
        currentSelectedNode = currentSelectedNode.next

    print("We cannot find this node")

  def delete(self, node):
    deleted = False
    currentSelectedNode = self.head
    while currentSelectedNode != self.tail:
      if currentSelectedNode == node:
        currentSelectedNode.delete()
        deleted = True 
        return deleted
      else:
        currentSelectedNode = currentSelectedNode.next

    return deleted

  def get_max(self):
    max = self.head.value 
    currentSelectedNode = self.head
    while currentSelectedNode != self.tail:
      if currentSelectedNode.value > max:
        max = currentSelectedNode.value 
      else:
        currentSelectedNode = currentSelectedNode.next

    return max 
