import time
from progress.bar import IncrementalBar
bar = IncrementalBar('Countdown', max = 20151121)
file1  = input("Please enter name of txt dock to create lib : ")
file2 = open(file1 , 'w')
lib = "1234567890qwertyuiopasdfghjklzxcvbnm~`!@#$%^&*()_-+=}{:;'?/><,."
start_time = time.time()
for a in lib:
	for b in lib:
		for c in lib:
			for d in lib:
				pswd = a + b + c + d
				#print(pswd , " --- %s seconds from start ---" % (time.time() - start_time))
				file2.write(pswd +'\n')
				bar.next()
				time.sleep(1)
bar.finish()
print("--- Ended in %s seconds ---" % (time.time() - start_time))