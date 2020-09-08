file1  = input("Please enter name of txt dock to create lib : ")
file2 = open(file1 , 'w')
text = input("Enter all information about person , separated by comma(',') : ")
words = text.split(",")
print(words)
for i in words:
	file2.write(i +'\n')
	for n in range(0,len(words)):
		file2.write(i+words[n]+'\n')
		file2.write(i+"_"+words[n]+'\n')
		file2.write(i+"-"+words[n]+'\n')
		file2.write(i+"."+words[n]+'\n')
		for a in range(0,len(words)):
			file2.write(i+words[n]+words[a]+'\n')
			file2.write(i+"_"+words[n]+"_"+words[a]+'\n')
			file2.write(i+"_"+words[n]+"."+words[a]+'\n')
			file2.write(i+"_"+words[n]+"-"+words[a]+'\n')

			file2.write(i+"."+words[n]+"-"+words[a]+'\n')
			file2.write(i+"."+words[n]+"."+words[a]+'\n')
			file2.write(i+"."+words[n]+"_"+words[a]+'\n')

			file2.write(i+"-"+words[n]+"_"+words[a]+'\n')
			file2.write(i+"-"+words[n]+"."+words[a]+'\n')
			file2.write(i+"-"+words[n]+"-"+words[a]+'\n')
