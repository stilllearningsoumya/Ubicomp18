import glob

filenames=glob.glob("WifiProcessData/FeatureScenario_*.txt")
file_out=open("WifiProcessData/total.txt","w")
for files in filenames:
	file_handle=open(files,"r")
	print(files)
	for lines in file_handle:
		lines=lines.strip("\r\n")
		file_out.write(lines+"\n")
	file_handle.close()
file_out.flush()
file_out.close()
		
