import json
import os
import fnmatch
 
files_json = [x for x in os.listdir('/estagio/2ºdesafio/dados') if x.endswith(".json")]
#print(files_json)
z=0
#print (files_json[z])
y = files_json[z]
#print (y)


#file = open(y, 'r')
#print(file.read( ))          

	#print (file2.read())


def findSNP(file1,file2):	
	""" juntar lista de ficheiros no ciclo do programa """

	count=0 #metodo do contador
	for line in  file2:
		count+=1 #para saltar informção desnecessária
		#print (line)
		if count==2:
			row_header=line
			row_header=row_header.split('"')
			row_header = row_header [3]
			row_header=row_header.split('EOT1D_')
			row_header = int(row_header [1])
			print (row_header, "-------------------------------------------------------")
		if count==15:
			gene1=line
			gene1=gene1.split('"')
			gene1 = gene1 [1]
		if count == 16:
			gene2=line
			gene2=gene2.split('"')
			gene2 = gene2 [1]
		if count == 17:
			gene3=line
			gene3=gene3.split('"')
			gene3 = gene3 [1]
		if count == 18:
			gene4=line
			gene4=gene4.split('"')
			gene4 = gene4 [1]
		if count == 19:
			gene5=line	
			gene5=gene5.split('"')
			gene5 = gene5 [1]
		if count == 20:
			gene6=line
			gene6=gene6.split('"')
			gene6 = gene6 [1]
	print ("All alelles: %s|%s|%s|%s|%s|%s" % (gene1,gene2,gene3,gene4,gene5,gene6))

	str = gene1
	str = str[0:8]
	gene_1 = str
	#print ("Read String is : ", gene_1)
	str = gene2
	str = str[0:8]
	gene_2 = str
	#print ("Read String is : ", gene_2)
	str = gene3
	str = str[0:8]
	gene_3 = str
	#print ("Read String is : ", gene_3)
	str = gene4
	str = str[0:8]
	gene_4 = str
	#print ("Read String is : ", gene_4)
	str = gene5
	str = str[0:8]
	gene_5 = str
	#print ("Read String is : ", gene_5)
	str = gene6
	str = str[0:8]
	gene_6 = str
	#print ("Read String is : ", gene_6)
	print ("First alelle: %s|%s|%s|%s|%s|%s" % (gene_1,gene_2,gene_3,gene_4,gene_5,gene_6))

	count = 0
	x = 0
	y = 0
	for line in file1:
		count += 1 # para saltar o header





		print (line)
		if gene1 in line:
			x = + 1
			print("found gene1")
			pass

		if gene2 in line:
			print("found gene2")
			x = x + 1
			pass

		if gene3 in line:
			print("found gene3")
			x = x + 1
			pass

		if gene4 in line:
			print("found gene4")
			x = x + 1
			pass

		if gene5 in line:
			print("found gene5")
			x = x + 1
			pass

		if gene6 in line:
			print("found gene6")
			x = x + 1
			pass  
		if gene_1 in line:
			y = + 1
			print("found gene_1")
			pass

		if gene_2 in line:
			print("found gene_2")
			y = y + 1
			pass

		if gene_3 in line:
			print("found gene_3")
			y = y + 1
			pass

		if gene_4 in line:
			print("found gene_4")
			y = y + 1
			pass

		if gene_5 in line:
			print("found gene_5")
			y = y + 1
			pass

		if gene_6 in line:
			print("found gene_6")
			y = y + 1
			break
					
	print ("all alelles: " "{0:.0%}".format(x/6))
	print ("First alelle: " "{0:.0%}".format(y/6))


def mysort(row_header): 
	"""ajudar o sort, na ordenação dos ficheiros pelos nomes"""
	row_header=row_header.split('_')
	row_header = row_header [1]
	row_header=row_header.split('-')
	row_header = row_header [0]
	return int(row_header)




file1 = open('HLAII_EOT1D_clinical.txt', 'r')
files_json.sort(key=mysort)
print (files_json)
for file in files_json:
	#print (file)
	file2 = open(file, 'r') 
	findSNP(file1,file2)	
	file2.close() 
file1.close()	