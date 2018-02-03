print "Hello"
date_file=open("dates.txt","r")
for dates in date_file:
	date=dates.strip("\r\n")
	print date
	in_file=open("wifiSLWP/"+date+".txt","r")
	for lines in in_file:
		print lines
		time=lines.strip("\r\n").split("|")[0]
		data=lines.strip("\r\n").split("|")[1:len(lines.strip("\r\n").split("|"))-1]
		out_file=open("wifiSLWP/"+date+"_"+time+".txt","w+")
		for i in data:
			data_2=i.split(",")
			string=""
			for j in data_2:
				if(j=="1.0000100001e-05"):
					j="0.00001"
				string+=j+" "
			out_file.write(string[0:len(string)-1])
			out_file.write("\n")
		out_file.flush()
		out_file.close()
	in_file.close()
date_file.close()
