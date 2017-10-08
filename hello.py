import sys


def addFn(val1, val2):
	return val1+val2

def divisionFn(val1, val2):
	return val1/val2

def main():
	#sys.exit(0)	
	print 'Hi'+sys.argv[1]
	print addFn(1,2)
	print divisionFn(3,2)
	a = ' vivek '
	b = 'test1'
	print a.upper()
	print a.lower()
	print len(a)
	print a.lower()
	print len(a)
	print ','.join([a,b])
	print a[1:4]
	print b[-1]
	val1 = sys.argv[2]
	val2 = sys.argv[3]
	val = ("Hello %s and %s" %(val1, val2))
	print val
	listObj = ['red', 'blue', 'green']
	print (listObj[1] + listObj[2])
	for i in listObj:
		print i
	
	if 'red' in listObj:
		print 'yes'
		for i in 'red':
			print i
	for i in range(100):
		print i
		
		
if __name__ == '__main__':
	main()