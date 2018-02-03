file_handle=open("stat1.txt","r")
cm=[]
time=[]
for lines in file_handle:
	lines=lines.strip("\r\n")
	if(lines.strip(" ")!=None or lines!=" "):
		if(lines.find("cache-misses",0,len(lines))!=-1):
			cm.append(int(lines.strip(" ").split(" ")[0].replace(",","")))
		elif(lines.find("seconds time elapsed",0,len(lines))!=-1):
			time.append(float(lines.strip(" ").split(" ")[0]))
file_handle.close()
print cm
print time
