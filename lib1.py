len = int(input("Please enter length of password : "))
num1 = pow(10 , len-1)
print( "Starts form", num1)
num2 = (pow(10,len) - 1)
print("Ends at " , num2)
file1  = input("Please enter name of txt dock to create lib : ")
file2 = open(file1 , 'w')
while(num1 != num2+1):
	file2.write(str(num1) +'\n')
	num1 += 1