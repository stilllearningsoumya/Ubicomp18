import glob

def runToCreateNetwork():
	name_to_integer_mapping={"rohit":"0","bidisha":"1","ayan":"2","snigdha":"3","satadal":"4","soumyajit":"5","samsung":"6","abhijit":"7"}
	date_file=open("dates.txt","r")
	for dates in date_file:
		dates=dates.strip("\r\n")
		print dates
		out_file=open("wifiSLWP/"+dates+".txt","w+")
		filenames=glob.glob("wifiSLWP/Splitted*"+dates+"*.txt")
		dict_1={}
		for files in filenames:
			net=""
			#print files.split("_")[2]
			net+=name_to_integer_mapping[files.split("_")[2]]+"," #User's in the network
			net+=name_to_integer_mapping[files.split("_")[3]] #User's in the network
			in_file=open(files,"r")
			for lines in in_file:
				lines=lines.strip("\r\n")
				time=lines.split(",")[0]
				inv_gain=lines.split(",")[1]
				if(time in dict_1.keys()):
					dict_1[time].append(net+","+inv_gain)
				else:
					dict_1[time]=[]
					dict_1[time].append(net+","+inv_gain)
			in_file.close()
		for i in dict_1.keys():
			out_file.write(i+"|")
			for j in dict_1[i]:
				out_file.write(j+"|")
			out_file.write("\n")
		out_file.flush()
		out_file.close()
	date_file.close()
