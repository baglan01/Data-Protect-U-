import time
from progress.bar import Bar 
bar = Bar('Progress', max = 646990183449)
file1  = input("Please enter name of txt dock to create lib : ")
file2 = open(file1 , 'w')
start_time = time.time()
for a in range(33,127):
	a1 = chr(a) 
	for b in range(33,127):
		b1 = chr(b)
		for c in range(33,127):
			c1 = chr(c)
			for d in range(33,127):
				d1 = chr(d)
				for e in range(33,127):
					e1 = chr(e)
					for f in range(33,127):
						f1 = chr(f)
						pswd = a1 + b1 + c1 + d1 + e1 + f1
						#print(pswd , " --- %s seconds from start ---" % (time.time() - start_time))
						file2.write(pswd +'\n')
						bar.next()
print("--- Ended in %s seconds ---" % (time.time() - start_time))