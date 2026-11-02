length = int(input("How long a queue do you want? "))

stack_array = [None] * length
front = 0
rear = 0

def enqueue(item):
  global front
  if is_full():
    print("Cant add any more items")
  else:
    stack_array[front] = item
    front +=1
    print("Sucessfully added", item)

def dequeue():
  global front
  if is_empty():
    print("Nothing to return")
    return None
  else:
    front-=1
    item = stack_array[front]
    return item

def size():
    return rear - front

def peek():
  if is_empty():
    print("Nothing in queue")
    return None
  else:
    return stack_array[front-1]

def is_full():
    return front == size

def is_empty():
    return rear == front

while True:
  option = int(input("Enter 1 to enqueue, 2 to dequeue, 3 to find the length, 4 to peek, 5 to check if full, 6 to check if empty, 7 to quit"))
  match option:
    case 1:
      item = input("What do you wish to add")
      enqueue(item)
    case 2:
      item = dequeue()
      print("Your item is:", item)
    case 3:
      queue_length = length
      print("The queue_length is", queue_length)
    case 4:
      item = peek()
      print("The next item will be:", item)
    case 5:
      if is_full():
        print("The queue is full")
      else:
        print("The queue is not full")
    case 6:
      if is_empty():
        print("The queue is empty")
      else:
        print("There are items in the queue")
    case 7:
      break
    case _:
        print("That isn't an option")
