

items = ["abc","xyz","pqri",123,456]

def separateList(items):
	str_item = []
	num_item = []

	for i in items:
		if isinstance(i,str):
			str_item.append(i)
		elif isinstance(i,int) or isinstance(i, float):
			num_item.append(i)
		else:
			pass
	return str_item,num_item



print(separateList(items))