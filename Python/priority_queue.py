#Start by doing 3 lists for each priority level, check if empty

length = int(input("How long a queue do you want? "))

queue_prio1_array = [None] * length
front_1 = 0
rear_1 = 0

queue_prio2_array = [None] * length
front_2 = 0
rear_2 = 0

queue_prio3_array = [None] * length
front_3 = 0
rear_3 = 0

def enqueue(item, priority):
	if is_full(priority):
		print("Cant add any more items")
	else:
		if priority == 1:
			global rear_1
			queue_prio1_array[rear_1] = item
			rear_1 += 1
		elif priority ==2:
			global rear_2
			queue_prio1_array[rear_2] = item
			rear_2 += 1
		else:
			global rear_3
			queue_prio1_array[rear_3] = item
			rear_3 += 1
		print("Sucessfully added ", item)


def dequeue():
	if is_empty(3) and is_empty(2) and is_empty(1):
				print("Nothing to return")
				return None
	elif is_empty(3) and is_empty(2):
		global front_1
		item = queue_prio1_array[front_1]
		front_1 += 1
		return item
	elif is_empty(3):
		global front_2
		item = queue_prio2_array[front_2]
		front_2 += 1
		return item
	else:
		global front_3
		item = queue_prio3_array[front_3]
		front_3 += 1
		return item

def size(priority):
	# reurn rear[pr]-front[pr]
	if priority == 3:
		return rear_3 - front_3
	elif priority == 2:
		return rear_2 - front_2
	else:
		return rear_1 - front_1

def peek(priority):
	if is_empty(priority):
		print("Nothing in queue")
		return None
	else:
		if priority == 3:
			return queue_prio3_array[front_3]
		elif priority == 2:
			return queue_prio2_array[front_2]
		else:
			return queue_prio1_array[front_1]

def is_full(priority):
	if priority == 3:
		return rear_3 == size(3)
	if priority == 2:
		return rear_2 == size(2)
	else:
		return rear_1 == size(1)


def is_empty(priority):
	if priority == 3:
		return rear_3 == front_3
	if priority == 2:
		return rear_2 == front_2
	else:
		return rear_1 == front_1


while True:
  option = int(input("Enter 1 to enqueue, 2 to dequeue, 3 to find the length, 4 to peek, 5 to check if full, 6 to check if empty, 7 to quit"))
  match option:
    case 1:
      item = input("What do you wish to add")
      priority = input("Which priority queue?")
      enqueue(item, priority)
    case 2:
      item = dequeue()
      print("Your item is:", item)
    case 3:
      queue_length = length
      print("The queue_length is", queue_length)
    case 4:
      priority = input("Which priority queue?")
      item = peek(priority)
      print("The next item will be:", item)
    case 5:
      priority = input("Which priority queue?")
      if is_full(priority):
        print("The queue is full")
      else:
        print("The queue is not full")
    case 6:
      priority = input("Which priority queue?")
      if is_empty(priority):
        print("The queue is empty")
      else:
        print("There are items in the queue")
    case 7:
      break
    case _:
        print("That isn't an option")
