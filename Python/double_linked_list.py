"""
tldr: do linked list, but also have a class for behind, and a tail pointer to point to the end instead of just a head
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

def prepend_node(head, value):
	# Add a new node at the head (begining, like appending to the front like a stack), and return the head
	new_head = Node(value)
	new_head.next = head
	# change the next one to point back to the added one
	if head != None:
		head.previous = new_head
	# returns the new head, same as assigning head to be the new head and then returning, but less lines
	return new_head

def append_node(tail, value):
	# Add a new node at the end, and returns the head
	try:
		tail.next = Node(value)
		tail.next.previous = tail
		return tail.next
	except AttributeError:
		tail = Node(value)
		return tail

def delete_node(head, value):
	start = head
	try:
		while head.next.data != value:
			head = head.next
		#make head "skip" over the value to be deleted, yeah its kinda memory inneficent and a "leak" as it doesn't fully delete but its fineee
		head.next = head.next.next
		head.next.previous = head
		return start
	except AttributeError:
		print("That item does not exist.")
		return start

def insert_after(head,  new_value, target_value, tail):
	# Adds the node with value new_value after target_value and returns head
	start = head
	try:
		while head.data != target_value:
			head = head.next
		temp = head.next
		head.next = Node(new_value)
		head.next.previous = head
		head.next.next = temp
		if temp != None:
			head.next.next.previous = head.next
		else:
			tail = head.next
		return start, tail
	except AttributeError:
		print("Empty list, can't add after", target_value)
		return start, tail

def print_list(head):
	nodes = []
	current = head
	while current is not None:
		nodes.append(str(current.data))
		current = current.next

	print(" -> ".join(nodes) + " -> None")

def main_menu():
	head = None
	tail = None
	while True:
		print("Linked List Operations:")
		print("  1. Append")
		print("  2. Prepend")
		print("  3. Insert after")
		print("  4. Delete")
		print("  5. Print")
		print("  6. Quit")
		choice = input("Enter your choice (1-6): ")

		if choice == '1':
			if head == None:
				value = int(input("  Enter value to append: "))
				head = append_node(head, value)
				tail = head
			else:
				value = int(input("  Enter value to append: "))
				tail = append_node(tail, value)

		elif choice == '2':
			value = int(input("  Enter value to prepend: "))
			head = prepend_node(head, value)
			if tail == None:
				tail = head

		elif choice == '3':
			value = int(input("  Enter value to insert: "))
			after = int(input("  Enter value this should be placed after: "))
			head, tail = insert_after(head, value, after, tail)

		elif choice == '4':
			value = int(input("  Enter value to delete: "))
			head = delete_node(head, value)

		elif choice == '5':
			print_list(head)

		elif choice == '6':
			print("Exiting.")
			break

		else:
			print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
	main_menu()
