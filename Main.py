class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
      node = Node(data)
      node.next = self.head
      self.head = node

  def pop(self) -> None:
      if(self.head is not None):
          self.head = self.head.next

  def status(self):
    ptr = self.head
    if(self.head is None):
        print("None")
    else:
        while (ptr):
            print(ptr.data, end="=>")
            ptr = ptr.next
        print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
