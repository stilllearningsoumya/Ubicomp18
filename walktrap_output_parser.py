import glob

path="slwp/"
filenames=glob.glob(path+"clustered_*.txt")
for files in filenames:
	#print files
	file_handle_in=open(files,"r")
	checkGroup=False
	groups=[]
	modularity=0.0
	noData=True
	for lines in file_handle_in:
		lines=lines.strip("\r\n")
		#print "Lines: "+lines
		noData=False		
		if(checkGroup==True):
			groups.append(lines.split("=")[1].replace('{',' ').replace('}',' ').strip(" "))
		elif(lines.find("modularity",0,len(lines))>-1):
			checkGroup=True
			modularity=float(lines.split(" ")[4])
		else:
			continue
	file_handle_in.close()
	if(noData==False):
		#print groups
		print modularity
		out_file="parsed_"+files.split("/")[1]
		file_handle_out=open(path+out_file,"w+")
		for group in groups:
			file_handle_out.write(group+"|")
		file_handle_out.write(str(modularity))
		file_handle_out.flush()
		file_handle_out.close()
