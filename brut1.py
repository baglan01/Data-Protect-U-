import time
pswd  = input("Please enter name of file with passwd : ")
pswd1 = open(pswd)
lib = input("Please enter name of your lib : ")
lib1 = open(lib)
passwd = pswd1.read()
print(passwd)
line = lib1.readline()
start_time = time.time()
while line:
	print("Now checking", line , " --- %s seconds from start ---" % (time.time() - start_time))
	if line == passwd :
		print("Your pswd was find : " , line)
		print("--- Ended in %s seconds ---" % (time.time() - start_time))
		break
	line = lib1.readline()