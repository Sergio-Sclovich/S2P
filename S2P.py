i = 1
array = []
with open("C:\\Users\\Ser\\Documents\\tesis\\Genetica_poblaciones\\AFLP\\info_global_25-11-16\\STRUCTURE\EVANO\\K4.indfile", "r") as f:
	for line in f:
		if line == '\n':
			print i
			output = open("K4r%s.Q" %i, "w")
			for row in array:
				output.write(row)
			output.close()
			i = i + 1
			array = []
		else:
			#print line
			array.append(line)
			


