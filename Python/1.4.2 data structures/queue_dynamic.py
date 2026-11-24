queue = []
maxItems = int(input("what is max items?"))

def enqueue(input):
	if maxItems > len(queue):
		queue.append(input)

def dequeue():
	if len(queue) > 0:
		return queue.pop(0)

def isEmpty():
	return len(queue) == 0
	#returns (return with no direct perameter is True) if the length of queue is 0

def isFull():
	return maxItems == len(queue)
	#same as isempty

while True:
  option = int(input("Enter 1 to enqueue, 2 to dequeue, 3 to check if full, 4 to check if empty, 5 to quit"))
  match option:
    case 1:
      item = input("What do you wish to add")
      enqueue(item)
    case 2:
      item = dequeue()
      print("Your item is:", item)
    case 3:
      if isFull():
        print("The queue is full")
      else:
        print("The queue is not full")
    case 4:
      if isEmpty():
        print("The queue is empty")
      else:
        print("There are items in the queue")
