class Node(object):
	def __init__(self, value):
		self.value = value 
		self.next = None

def create_linkList(n):
	head = Node(1)
	pre = head
	for i in range(2, n+1):
		newNode = Node(i)
		pre.next= newNode
		pre = newNode
	pre.next = head
	return head

n = 5 #總的個數
m = 2 #數的數目
if m == 1: #如果是1的话，特殊處理，直接輸出
	print (n)  
else:
	head = create_linkList(n)
	pre = None
	cur = head
	while cur.next != cur: #终止條件是節點的下一个節點指向本身
		for i in range(m-1):
			pre =  cur
			cur = cur.next
		print (cur.value)
		pre.next = cur.next
		cur.next = None
		cur = pre.next
	print (cur.value)