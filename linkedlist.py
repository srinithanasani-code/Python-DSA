class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList():
  def __init__(self,data):
    self.head=None
    self.size=0
  def add(self,data):
    if self.head==None:
      self.head=Node(data)
      self.size+=1
      return
    cN=self.head
    while cN.next is not None:
      cN=cN.next
    cN.next=Node(data)
    self.size+=1
  def traverse(self):
    if self.head==None:
      print()
      return
    cN=self.head
    while cN.next is not None:
      print(cN.data,end='->')
      cN=cN.next
    print(cN.data)
  def search(self,data):
    if self.head==None:
      print("no elements in LL")
      return
    ind=0
    cn=self.head
    while cn.next is not None:
      if cn.data==data:
       print(f'element {data} is found at {ind} index')
       return
      cn=cn.next
      ind+=1
    if cn.data==data:
      print(f'element {data} is found at {ind} index')
      return
    print('element not found')  
  def len(self):
    return self.size
  def begin(self,data):
    node=Node(data)
    node.next=self.head
    self.head=node
  def delbegin(self):
    if self.head==None:
      return
    else:
      self.head=self.head.next
  def delLast(self):
    if self.head==None:
     return
    cN=self.head
    while cN.next is not None:
      cN=cN.next
    cN.next=None
    self.size-=1
      

ll=LinkedList(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
#print(ll.head.next.data)
ll.traverse()
ll.search(30)
print(ll.len())
ll.begin(100)
ll.traverse()
ll.delbegin()
ll.traverse()
ll.delLast()