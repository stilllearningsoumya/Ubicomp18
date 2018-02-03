import glob

def diceCoefficient(set_1,set_2):
	return (2.0*float(len(set_1.intersection(set_2)))/(float(len(set_1))+float(len(set_2))))

def calculateScore(rel,ret):
	avg=0.0
	for i in range(len(ret)):
		maxValue=-1.0
		for j in range(len(rel)):
			diceValue=diceCoefficient(set(ret[i]),set(rel[j]))
			if(diceValue>maxValue):
				maxValue=diceValue
		avg+=maxValue		
	return avg/float(len(ret))

def evaluateProxy(path):
	avg=0.0
	count=0
	avgMod=0.0
	#path="Scenario1/"
	thresh_1=0.3
	thresh_2=0.01
	filenames_for_evaluation=glob.glob(path+"parsed_clustered_*.txt")
	print len(filenames_for_evaluation)
	for files in filenames_for_evaluation:
		print files
		specific_file=files.split("_")[2].split(".")[0].split("s")[0]
		print specific_file
		file_ground_truth=open("groundtruth/groundtruth_"+specific_file+".txt","r")
		relevant=[]
		for line in file_ground_truth:
			line=line.strip("\r\n")
			data=line.split("|")
			for elem in data:
				elem_1=elem.split(",")
				temp=[]
				for el in elem_1:
					temp.append(el.strip(" "))
				relevant.append(temp)
		file_ground_truth.close()
		print relevant
		file_eval=open(files,"r")
		retrieved=[]
		for line in file_eval:
			line=line.strip("\r\n")
			data=line.split("|")
			Q=float(data[len(data)-1])
			for i in range(len(data)-1):
				elem_1=data[i].split(",")
				temp=[]
				for el in elem_1:
					temp.append(el.strip(" "))
				retrieved.append(temp)
		file_eval.close()
		print retrieved
		avg+=calculateScore(relevant,retrieved)
		avgMod+=Q
		count+=1
		print "Average F1-Score: "+str(calculateScore(relevant,retrieved))+" Modularity: "+str(Q)
	avg=avg/float(count)
	avgMod=avgMod/float(count)
	print "Overall"
	print str(avg)+","+str(avgMod)
evaluateProxy("slwp/")
