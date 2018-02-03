import glob
#from memory_profiler import profile

###################################################################################################################
def diceCoefficient(set_1,set_2):
	return (2.0*float(len(set_1.intersection(set_2)))/(float(len(set_1))+float(len(set_2))))

def calculateScore(rel,ret):
	# print rel
	# print ret
	avg=0.0
	for i in range(len(ret)):
		maxValue=-1.0
		for j in range(len(rel)):
			diceValue=diceCoefficient(set(ret[i]),set(rel[j]))
			if(diceValue>maxValue):
				maxValue=diceValue
		avg+=maxValue		
	return avg/float(len(ret))
###################################################################################################################
#@profile
def groupSense(thresh_1,thresh_2,thresh_3,path_wifi,path_audio):
	avg=0.0
	avgMod=0.0
	count=0
	filenames_for_evaluation=glob.glob(path_wifi+"parsed_clustered_*.txt")
	for files in filenames_for_evaluation:
		#print files
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
		Q=-1.0
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
			print "Proximity: "+str(Q)
		file_eval.close()
		print retrieved
		if(Q>=thresh_1):
			print "Condition 1: "
			avg+=calculateScore(relevant,retrieved)
			avgMod+=Q
			print str(calculateScore(relevant,retrieved))+","+str(Q)
			count+=1
			try:
				#Audio
				file_audio=open(path_audio+"parsed_clustered_"+specific_file+"sData.txt","r")
				audio_ret=[]
				for line in file_audio:
					line=line.strip("\r\n")
					data=line.split("|")
					Q_1=float(data[len(data)-1])
					print "Audio: "+str(Q_1)
					for i in range(len(data)-1):
						elem_1=data[i].split(",")
						temp=[]
						for el in elem_1:
							temp.append(el.strip(" "))
						audio_ret.append(temp)
				file_audio.close()
				print audio_ret
				if(Q_1>thresh_3 or abs(Q_1)<0.00001):
					#avg+=calculateScore(relevant,audio_ret)
					#avgMod+=Q_1
					print str(calculateScore(relevant,audio_ret))+","+str(Q_1)
				else:
					avg+=0.0 #Failure
					#print str(0.0)+","+str(Q_1)
				count+=1
			except Exception as e:
				print e
				pass	
		elif((Q<thresh_1 and Q>=thresh_2) or abs(Q)<0.00001):
			print "Condition 2: "
			try:
				#Audio
				file_audio=open(path_audio+"parsed_clustered_"+specific_file+"sData.txt","r")
				audio_ret=[]
				for line in file_audio:
					line=line.strip("\r\n")
					data=line.split("|")
					Q_1=float(data[len(data)-1])
					print "Audio: "+str(Q_1)
					for i in range(len(data)-1):
						elem_1=data[i].split(",")
						temp=[]
						for el in elem_1:
							temp.append(el.strip(" "))
						audio_ret.append(temp)
				file_audio.close()
				print audio_ret
				if(Q_1>thresh_3 or abs(Q_1)<0.00001):
					avg+=calculateScore(relevant,audio_ret)
					avgMod+=Q_1
					print str(calculateScore(relevant,audio_ret))+","+str(Q_1)
				else:
					avg+=0.0 #Failure
					#print str(0.0)+","+str(Q_1)
				count+=1
			except Exception as e:
				print e
				pass

		else:
			#print "Hello"
			avg+=0.0 #Failure
			count+=1
	if(count!=0.0):
		avg=avg/float(count)
		avgMod=avgMod/float(count)
	print "Overall:"
	print str(avg)+","+str(avgMod) 

threshold_1 = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
threshold_2 = [0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01]
threshold_3 = [0.001]

def evaluateEntireSystem(path_wifi,path_audio):
#for i in range(len(threshold_1)):
	groupSense(0.3,0.01,0.01,path_wifi,path_audio)

if __name__ == '__main__':
    evaluateEntireSystem("slwp/","audio/")
