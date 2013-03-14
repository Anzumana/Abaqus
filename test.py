inputFile = open('README')

outputFile = open('upper.txt','w') 
lines = inputFile.readlines()
for line in lines:
	newLine = line.upper()
	outputFile.write(newLine)

inputFile.close()
outputFile.close()
