class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_node(value):
	# This returns a dictionary of each node with it's value and pointer
	return Node(value)

def prepend_node(head, value):
	# Add a new node at the head (begining, like appending to the front like a stack), and return the head
	new_head = Node(value)
	new_head.next = head
	# returns the new head, same as assigning head to be the new head and then returning, but less lines
	return new_head

def append_node(head, value):
	# Add a new node at the end, and returns the head
	start = head
	while head.next != None:
		head = head.next
	head.next = Node(value)
	head = start

def delete_node(head, value):
	start = head
	while head.next.data != value:
		head = head.next
	#make head "skip" over the value to be deleted, yeah its kinda memory inneficent and a "leak" as it doesn't fully delete but its fineee
	head.next = head.next.next
	return start


""""
done up until here.
"""

def insert_after(head,  new_value, target_value):
	# Adds the node with value new_value after target_value and returns head
	if head is None:
		print("Empty list, can't add after", target_value)
		return None

	# Start traversal to find the target node
	current = head
	while current is not None:
		# Check if the current node is the target
		if current['value'] == target_value:
			# Found the target node. Insert the new node after it.
			new_node = create_node(new_value)

			# 1. Link new node to the rest of the list
			new_node['next'] = current['next']

			# 2. Link the current (target) node to the new node
			current['next'] = new_node

			print("Inserted", new_value, "after", target_value)
			return head

		# Move to the next node
		current = current['next']

	# Target node is not in list, so can't add after
	print(f"Error: Value {target_value} not found. Cannot insert.")
	return head

def print_list(head):

	nodes = []
	current = head
	while current is not None:
		nodes.append(str(current['value']))
		current = current['next']

	print(" -> ".join(nodes) + " -> None")

def main_menu():

	head = None

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
			value = int(input("  Enter value to append: "))
			head = append_node(head, value)

		elif choice == '2':
			value = int(input("  Enter value to prepend: "))
			head = prepend_node(head, value)

		elif choice == '3':
			value = int(input("  Enter value to insert: "))
			after = int(input("  Enter value this should be placed after: "))
			head = insert_after(head, value, after)

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
