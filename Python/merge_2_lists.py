#test values

list1 = [1,2,5,6]
list2 = [3,4]

def mergelists(list1, list2):
	end = False
	mergedlist = []
	while end == False:
		if len(list1) != 0 and len(list2) != 0:
			l1 = list1[0]
			l2 = list2[0]
			
			if l1 <= l2:
				mergedlist.append(list1.pop(0))
			else:
				mergedlist.append(list2.pop(0))
				
		elif len(list1) != 0:
			mergedlist.append(list1.pop(0))
			
		if len(list2) != 0:
			mergedlist.append(list2.pop(0))
			
		else:
			return mergedlist

print(mergelists(list1, list2))
