import sys


def main():
	print 'List'
	listObj = ['vivek', 'admin', 'test', 'xyz']
	listObj.append('pqr')
	listObj.insert(1,'qwe')
	print sorted(listObj)	
	print listObj
	print listObj.index('admin')
	listObj.sort()
	print listObj
	listObj.reverse()
	print listObj
	listObj.pop(3)
	print listObj
	
if __name__ == '__main__':
	main()